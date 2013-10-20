# Echobox is essentially "put in a quote, get out a quote".  Might not be perfect for everyone, but it's a fun set of commands
import random

name = 'echobox'
enabled = True
operator = False

def cmd(self, c, e, line, message_source, target):
    if len(line) == 1 or len(line[1]) < 2:
        self.send(c, target, "Error - Echobox needs a valid input quote to function")
        return
    echobox_file = file('echobox.txt', 'r+')
    echobox_lines = echobox_file.readlines()
    if e.arguments[0].split(" ", 1)[1] + "\n" in echobox_lines:
        self.send(c, target, "Error - Quote already in Echobox")
        echobox_file.close()
        return
    self.send(c, target, u'\u0002Echobox: \u000F' + self.eval(c, e, random.choice(echobox_lines).replace("\n", ""), target))
    echobox_file.close()
    echobox_lines.append(e.arguments[0].split(" ", 1)[1] + "\n")
    echobox_file = file('echobox.txt', 'w')
    echobox_file.writelines(echobox_lines)
    echobox_file.close()
    self.last = e.source.nick

def init(self):
    self.last_echobox = ""
    
def evaluator(self, c, e, s, target):
    if '$ECHOBOX' in s:
        with open('echobox.txt', 'r') as f:
            s = ''.join(s).replace("$ECHOBOX", ''.join(self.eval(c, e, random.choice(f.readlines()).replace("\n", ""), target)))
    return s

def on_quit(self, c, e):
    if e.source.nick == self.last_echobox:
        self.last_echobox = ""