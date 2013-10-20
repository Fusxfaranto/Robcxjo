name = 'join'
enabled = False
operator = True

def cmd(self, c, e, line, message_source, target):
        c.join(line[1])

    