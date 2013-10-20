name = 'set'
enabled = False
operator = True

def cmd(self, c, e, line, message_source, target):
        if len(line[1].split(" ")) > 2:
            l = getattr(self, line[1].split(" ")[0])
            l[int(line[1].split(" ")[1])] = line[1].split(" ")[2]
        else:
            setattr(self, line[1].split(" ", 1)[0], line[1].split(" ", 1)[1])
                    
    