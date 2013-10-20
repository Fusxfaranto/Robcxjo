import pickle

name = 'enable'
enabled = False
operator = True

def cmd(self, c, e, line, message_source, target):
    if len(line) == 1:
        self.send(c, target, "Error - Not enough arguments")
    else:
        self.enabled_commands[target.lower()][line[1]] = True
        try:
            with open('enabled_commands.txt', 'wb') as f:
                pickle.dump(self.enabled_commands, f)
        except:
            open('enabled_commands.txt', 'a').close()
            with open('enabled_commands.txt', 'wb') as f:
                pickle.dump(self.enabled_commands, f)
        self.send(c, target, line[1] + " enabled")
                
    