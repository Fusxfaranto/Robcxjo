name = 'kick'
enabled = False
operator = True

def cmd(self, c, e, line, message_source, target):
        if len(line) == 1:
            c.kick(target, e.source.nick, "Kick requested from " + e.source.nick)
        elif len(line[1].split(" ")) == 1:
            c.kick(target, line[1], "Kick requested from " + e.source.nick)
        elif len(line[1].split(" ")) == 2:
            c.kick(line[1].split(" ")[0], line[1].split(" ")[1], "Kick requested from " + e.source.nick)
        elif len(line[1].split(" ")) > 2:
            c.kick(line[1].split(" ")[0], line[1].split(" ")[1], "Kick requested from " + e.source.nick + " with message: " + line[1].split(" ", 2)[2])
            

    