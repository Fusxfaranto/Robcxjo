#! /usr/bin/env python
# -*- coding: utf-8 -*-

import irc.bot
import irc.strings
import irc.events
import ConfigParser
import logging
import pickle
import sys
import os
from time import strftime, sleep

import plugins

class Bot(irc.bot.SingleServerIRCBot):
    def __init__(self, config, testing=False):
        self.config = config
        irc.bot.SingleServerIRCBot.__init__(self, [(self.config['server'], self.config['port'])], self.config['nickname'], self.config['nickname'])
        self.channel_list = self.config['channel_list']
            
        self.nickmask = irc.client.NickMask(self.config['nickmask'])
        self.operators = self.config['operators']
        self.operators.append(self.nickmask)
        self.password = self.config['password']
        
        # disabled_message is a lambda function taking the source nick as an argument, giving a bit more flexibility than just a string
        self.disabled_message = self.config['disabled_message']
        
        self.on_event_commands = {}
        self.load_commands()
        try:
            with open("enabled_commands.txt", "rb") as f:
                self.enabled_commands = pickle.loads(f.read())
        except:
            self.enabled_commands = {}
        try:
            with open("nickmask_disables.txt", "rb") as f:
                self.nickmask_disables = pickle.loads(f.read())
        except:
            self.nickmask_disables = {}
        try:
            if not testing:
                with open("channels.txt", "rb") as f:
                    self.channel_list += pickle.loads(f.read())
        except:
            self.channel_list = {}
            
        self.users_in_channel = {}
        self.multiline_names = {}
        self.last_line = {}
        
        for f in self.init_commands:
            self.init_commands[f](self)
        
    def load_commands(self):
        self.default_enables = {}
        self.command_names = {}
        self.commands = {}
        self.inline_commands = {}
        self.init_commands = {}
        self.eval_commands = {}
        self.on_event_commands = {}
        
        def handler_maker(event):
            def handler(c, e):
                for f in self.on_event_commands[event]:
                    if self.enabled_for_sender(c, e, f, e.target, False):
                        self.on_event_commands[event][f](self, c, e)
            return handler
        
        for i in plugins.plugin_list:
            if func_exists(getattr(plugins, i), 'cmd'):
                self.commands[',' + getattr(plugins, i).name] = getattr(plugins, i).cmd
                self.command_names[',' + getattr(plugins, i).name] = i
            for event in irc.events.all:
                if func_exists(getattr(plugins, i), 'on_' + event):
                    self.on_event_commands[event] = {}
                    self.on_event_commands[event][i] = getattr(getattr(plugins, i), 'on_' + event)
                    self.ircobj.add_global_handler(event, handler_maker(event), 100)
            if func_exists(getattr(plugins, i), 'init'):
                self.init_commands[i] = getattr(plugins, i).init
            if func_exists(getattr(plugins, i), 'inline'):
                self.inline_commands[i] = getattr(plugins, i).inline
            if func_exists(getattr(plugins, i), 'evaluator'):
                self.eval_commands[i] = getattr(plugins, i).evaluator
            self.default_enables[i] = getattr(plugins, i).enabled
        
    def on_welcome(self, c, e):
        self.send(c, "NickServ", "IDENTIFY " + self.password)
        irc.client.VERSION = "1"  # For some reason crashes on joining rizon without this
        self.channel_check(c)
        
    def on_disconnect(self, c, e):
        while not self.connection.is_connected():
            self.jump_server()
            sleep(5)
        
    def on_join(self, c, e):
        self.beacon = False
        for i in self.channels:
            if i not in self.enabled_commands:
                self.enabled_commands[i.lower()] = self.default_enables.copy()
                with open('enabled_commands.txt', 'wb') as f:
                    pickle.dump(self.enabled_commands, f)
        self.multiline_names[e.target.lower()] = False
        try:
            if not e.source.nick in self.users_in_channel[e.target.lower()]:
                self.users_in_channel[e.target.lower()].append(e.source.nick)
        except KeyError:
            pass
        
    def on_part(self, c, e):
        self.multiline_names[e.target.lower()] = False
        try:
            if e.source.nick in self.users_in_channel[e.target.lower()]:
                self.users_in_channel[e.target.lower()].remove(e.source.nick)
        except KeyError:
            pass
        
    def on_quit(self, c, e):
        try:
            for i, d in self.users_in_channel.iteritems():
                if e.source.nick in d:
                    self.users_in_channel[i].remove(e.source.nick)
        except KeyError:
            pass
        
    def on_nick(self, c, e):
        try:
            for i, d in self.users_in_channel.iteritems():
                if e.source.nick in d:
                    self.users_in_channel[i][self.users_in_channel[i].index(e.source.nick)] = e.target
        except KeyError:
            pass
        
    def on_kick(self, c, e):
        self.multiline_names[e.target.lower()] = False
        try:
            if e.arguments[0] in self.users_in_channel[e.target.lower()]:
                self.users_in_channel[e.target.lower()].remove(e.arguments[0])
        except KeyError:
            pass
        self.channel_check(c)
        
    def on_mode(self, c, e):
        if e.arguments[0] == "+b" and "Robcxjo" in e.arguments[1]:
            self.channel_list.remove(e.target)
        elif e.arguments[0] == "-b" and "Robcxjo" in e.arguments[1]:
            try:
                self.channel_list.add(e.target)
            except:
                pass
        self.channel_check(c)
        
    def on_invite(self, c, e):
        c.join(e.arguments[0])
        self.channel_list.append(e.arguments[0])
        self.channel_check(c)
        
    def on_pubmsg(self, c, e):
        print "public message: " + e.target + " | [" + strftime("%H:%M:%S") + "] <" + e.source.nick + "> " + e.arguments[0]
        self.command(c, e, "public")
        
    def on_privmsg(self, c, e):
        print "private message: [" + strftime("%H:%M:%S") + "] <" + e.source.nick + "> " + e.arguments[0]
        self.command(c, e, "private")
        
    def on_pubnotice(self, c, e):
        print "public notice: " + e.target + " | [" + strftime("%H:%M:%S") + "] <" + e.source.nick + "> " + e.arguments[0]
        
    def on_privnotice(self, c, e):
        print "private notice: [" + strftime("%H:%M:%S") + "] <" + e.source.nick + "> " + e.arguments[0]
        
    def on_namreply(self, c, e):
        if self.multiline_names[e.arguments[1].lower()]:
            self.users_in_channel[e.arguments[1].lower()].append(e.arguments[2].replace("~", "").replace("&", "").replace("@", "").replace("%", "").replace("+", "").split(" ")[:-1])
        else:
            self.users_in_channel[e.arguments[1].lower()] = e.arguments[2].replace("~", "").replace("&", "").replace("@", "").replace("%", "").replace("+", "").split(" ")[:-1]
        self.multiline_names[e.arguments[1].lower()] = True
        print "namreply: " + e.arguments[0] + " | " + e.arguments[1] + " | " + e.arguments[2]
        if self.beacon:
            self.send(c, e.arguments[1], u'\u0002BEACON: \u000F' + e.arguments[2].replace("~", "").replace("&", "").replace("@", "").replace("%", "").replace("+", ""))
            self.beacon = False
                
    def on_ctcp(self, c, e):
        s = "ctcp: " + e.target + " | [" + strftime("%H:%M:%S") + "] <" + e.source.nick + "> "
        for i in e.arguments:
            s += i + " | "
        print s[:-3]
        
        try:
            if len(e.arguments) > 1 and e.arguments[0] == u'ACTION' and u'cums on Robcxjo' in e.arguments[1] and self.cum_counter < 15 and self.enabled_commands[e.target.lower()]["misc"]:
                c.ctcp(u'ACTION', e.target, u'cums on ' + e.source.nick)
                self.cum_counter += 1
            else:
                self.cum_counter = 0
        except KeyError:
            pass
            
    def channel_check(self, c):
        for i in self.channel_list:
            if not i in self.channels:
                c.join(i)
        with open('channels.txt', 'wb') as f:
            pickle.dump(self.channel_list, f)
                
    def send(self, c, target, msg):
        if target[0] == "#":
            print "public message: " + target + " | [" + strftime("%H:%M:%S") + "] <Robcxjo> " + msg
            c.privmsg(target, msg)
            self.command(c, irc.client.Event("pubmsg", self.nickmask, target, [msg]), "public")
        else:
            print "private message: " + target + " | [" + strftime("%H:%M:%S") + "] <Robcxjo> " + msg
            c.privmsg(target, msg)
            self.command(c, irc.client.Event("privmsg", self.nickmask, target, [msg]), "private")
        
    def send_notice(self, c, target, msg):
        if target[0] == "#":
            print "public notice: " + target + " | [" + strftime("%H:%M:%S") + "] <Robcxjo> " + msg
        else:
            print "private notice: " + target + " | [" + strftime("%H:%M:%S") + "] <Robcxjo> " + msg
        c.notice(target, msg)
        
    def command(self, c, e, message_source):                     # TODO: ,dice command
        self.channel_check(c)
        
        if self.block and e.source in self.operators and e.arguments[0] != ",block":
            self.block_text += e.arguments[0] + "\n"
            return
        if self.block and not e.source in self.operators:
            return
        
        if message_source == "public":
            target = e.target
            self.multiline_names[target.lower()] = False
        else:
            target = e.source.nick
        
        line = self.eval(c, e, e.arguments[0], target).split(" ", 1)
        
        line[0] = line[0].lower()
        
        
        try:
            for f in self.inline_commands:
                if self.enabled_for_sender(c, e, f, e.target, False):
                    self.inline_commands[f](self, c, e, line, message_source, target)
                
            if line[0][0] == ",":
                if not self.enabled_for_sender(c, e, self.command_names[line[0]], target):
                    return
                try:
                    if func_exists(getattr(plugins, self.command_names[line[0]]), 'cmd'):
                        self.commands[line[0]](self, c, e, line, message_source, target)
                    else:
                        self.commands[line[0]](c, e, line, message_source, target)
                except AttributeError:
                    self.commands[line[0]](c, e, line, message_source, target)
        except IndexError:
            print "indexerror"
        except KeyError:
            try:
                if message_source == "private":
                    if line[0][0] == ",":
                        if not self.enabled_for_sender(c, e, self.command_names[line[0]], target):
                            return
                        try:
                            if func_exists(getattr(plugins, self.command_names[line[0]]), 'cmd'):
                                self.commands[line[0]](self, c, e, line, message_source, target)
                            else:
                                self.commands[line[0]](c, e, line, message_source, target)
                        except AttributeError:
                            self.commands[line[0]](c, e, line, message_source, target)
            except KeyError:
                print "keyerror"
            except IndexError:
                print "indexerror (pm)"
                
#TODO: public key shit

# helper methods
    def eval(self, c, e, s, target):
        for f in self.eval_commands:
            if self.enabled_for_sender(c, e, f, e.target, False):
                s = self.eval_commands[f](self, c, e, s, target)
                
        return s
    
    def enabled_for_sender(self, c, e, command, target, verbose=True):
        if target is None:
            return True         # Events like quit have to manage enablements themselves, it doesn't really work with the system as it is otherwise
        if getattr(plugins, command).operator and not e.source in self.operators:
            if verbose:
                self.send(c, target, self.disabled_message(e.source.nick))
            return False
        if target != e.source.nick and target.lower() in self.enabled_commands and not self.enabled_commands[target.lower()][command]:
            if verbose:
                if e.source in self.operators:
                    return True
                else:
                    self.send(c, target, self.disabled_message(e.source.nick))
            return False
        source = None
        if '!' in e.source:
            if e.source.lower() in self.nickmask_disables:
                source = e.source.lower()
            elif e.source.nick.lower() in self.nickmask_disables:
                source = e.source.nick.lower()
            elif e.source.user.lower() in self.nickmask_disables:
                source = e.source.user.lower()
            elif e.source.host.lower() in self.nickmask_disables:
                source = e.source.host.lower()
            elif e.source.userhost.lower() in self.nickmask_disables:
                source = e.source.userhost.lower()
            if source != None and command in self.nickmask_disables[source]:
                if verbose:
                    self.send(c, target, self.disabled_message(e.source.nick))
                return False
        return True




def func_exists(func_class, func):
    try:
        return hasattr(func_class, func) and callable(getattr(func_class, func))
    except:
        return False

def main():
    try:
        os.remove('log.log')
    except OSError as e:
        print e
    
    logging.basicConfig(filename='log.log',level=logging.DEBUG)
    
    config = {}
    execfile('config.cfg', config)
    
    # Set up like this so i can just uncomment a line to test
    testing = False
    #testing = True
    
    bot = Bot(config, testing)
    
    done = 0
    
    while done == 0:
        try:
            bot.start()
        except UnicodeDecodeError:
            print "unicodedecodeerror"
        else:
            done = 1
    

if __name__ == '__main__':
    x = main()
    #if x == 1:
    #    print 'aojawrgjio'
    #    os.execl(sys.executable, sys.executable, * sys.argv)
