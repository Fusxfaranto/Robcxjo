name = 'say'
enabled = False
operator = True

def cmd(self, c, e, line, message_source, target):
        s = line[1].split(" ", 1)
        self.send(c, s[0], s[1])
    
    