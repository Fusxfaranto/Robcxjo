name = 'beacon'
enabled = False
operator = False

def cmd(self, c, e, line, message_source, target):
        self.beacon = True
        c.send_raw("NAMES " + target)

def init(self):
    self.beacon = False