# -*- coding: utf-8 -*-
# This is just a lot of inside-joke type of scripts, so I don't know how much use someone else will get out of it
from time import sleep

name = 'misc'
enabled = False
operator = False

def inline(self, c, e, line, message_source, target):
    if line[0] == "@seen":
        sleep(1)
        self.send(c, target, "rip")
    elif line[0] == "!etoke":
        sleep(1)
        self.send(c, target, "!in")
    if "denko" in e.arguments[0] or "Denko" in e.arguments[0]:
        self.send(c, target, "(´･ω･`)")
        
#    if "o_O" in line[0]:
#        self.send(c, target, "http://i.imgur.com/IK8Rh03.png")
#    if ":p" in line[0]:
#        self.send(c, target, "http://i.imgur.com/hDC74L5.png")
#    if ":(" in line[0]:
#        self.send(c, target, "http://i.imgur.com/jajX0pB.jpg")