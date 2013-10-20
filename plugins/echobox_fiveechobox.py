import random

name = 'fiveechobox'
enabled = True
operator = False

def cmd(self, c, e, line, message_source, target):
        with open('echobox.txt', 'r') as f:
            l = f.readlines()
            random.shuffle(l)
            for i in range(5):
                self.send(c, target, u'\u0002Echobox: \u000F' + self.eval(c, e, l.pop().replace("\n", ""), target))

    