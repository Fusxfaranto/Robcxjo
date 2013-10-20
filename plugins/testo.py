name = 'testo'
enabled = True
operator = False

def cmd(self, c, e, line, message_source, target):
    self.send(c, target, "testo")
    
def on_privnotice(self, c, e):
    if 'testo' in e.arguments[0]:
        self.send_notice(c, e.source.nick, "testo")
        
def on_invite(self, c, e):
    print 'invite'
    
def on_pubmsg(self, c, e):
    print 'pubmsg'
        
def init(self):
    print 'testo'
    
def inline(self, c, e, line, message_source, target):
    if 'testo' in ''.join(line):
        print 'inline te sto'
        
def evaluator(self, c, e, s, target):
    s = ''.join(s).replace("$TESTO", 'poopy butts', 1)
    
    while "$TESTO" in s:
        s = s.replace("$TESTO", 'poopy butts', 1)
        
    return s
