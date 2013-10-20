name = 'block'
enabled = False
operator = True

def cmd(self, c, e, line, message_source, target):
        if self.block:
            self.block = False
        else:
            self.block_text = ""
            self.block = True

def init(self):
    self.block = False
    self.block_text = ""