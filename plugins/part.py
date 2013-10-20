name = 'part'
enabled = False
operator = True

def cmd(self, c, e, line, message_source, target):
        if len(line) > 1:
            c.part(line[1])
        else:
            c.part(target)

    