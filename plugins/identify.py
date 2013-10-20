name = 'identify'
enabled = False
operator = True

def cmd(self, c, e, line, message_source, target):
        self.send(c, "NickServ", "IDENTIFY cockmongrel")

    