# -*- coding: utf-8 -*-
name = 'meter'
enabled = True
operator = False

def cmd(self, c, e, line, message_source, target):
        try:
            if "," in line[1]:
                l = line[1].split(",", 1)
            else:
                l = line[1].split(" ", 1)
            level = int(hash(l[0]) + hash(l[1].strip())) % 101
            s = "|"
            for i in xrange(0, 10):
                if round(level / 10.0) > i:
                    s += "■"
                else:
                    s += "□"
            self.send(c, target, l[1].strip() + "'s " + l[0] + " level: " + s + "| (" + str(level) + "%)")
        except IndexError:
            self.send(c, target, "Error - invalid argument(s)")
    
    