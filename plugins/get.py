name = 'get'
enabled = False
operator = True

def cmd(self, c, e, line, message_source, target):
        if len(line[1].split(" ", 1)) > 1:
            self.send(c, target, str(getattr(self, line[1].split(" ", 1)[0])[int(line[1].split(" ", 1)[1])]))
        else:
            self.send(c, target, str(getattr(self, line[1])))

    