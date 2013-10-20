name = 'eval'
enabled = True
operator = False

def cmd(self, c, e, line, message_source, target):
        self.send(c, target, "Eval: " + line[1])

    