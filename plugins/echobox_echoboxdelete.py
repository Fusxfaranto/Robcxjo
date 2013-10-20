# Just deletes the last echobox quote put in
name = 'echoboxdelete'
enabled = True
operator = False

def cmd(self, c, e, line, message_source, target):
        if e.source.nick == self.last_echobox or e.source in self.operators:
            echobox_file = file('echobox.txt', 'r')
            echobox_lines = echobox_file.readlines()
            echobox_file.close()
            echobox_lines.pop()
            echobox_file = file('echobox.txt', 'w')
            echobox_file.writelines(echobox_lines)
            echobox_file.close()
            self.send(c, target, "Previous quote deleted")
            self.last_echobox = ""
        else:
            self.send(c, target, "Error: quote can only be deleted by the person who put it in")
        
    