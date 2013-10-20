import pickle

name = 'resetenables'
enabled = False
operator = True

def cmd(self, c, e, line, message_source, target):
        if len(line) > 1:
            self.enabled_commands[line[1].lower()] = self.default_enables.copy()
            try:
                with open('enabled_commands.txt', 'wb') as f:
                    pickle.dump(self.enabled_commands, f)
            except:
                open('enabled_commands.txt', 'a').close()
                with open('enabled_commands.txt', 'wb') as f:
                    pickle.dump(self.enabled_commands, f)
        else:
            for i in self.channels:
                self.enabled_commands[i.lower()] = self.default_enables.copy()
                try:
                    with open('enabled_commands.txt', 'wb') as f:
                        pickle.dump(self.enabled_commands, f)
                except:
                    open('enabled_commands.txt', 'a').close()
                    with open('enabled_commands.txt', 'wb') as f:
                        pickle.dump(self.enabled_commands, f)


def on_pubmsg(self, c, e):
    if e.arguments[0].split(' ', 1)[0] == ',emergencyresetenables':
        for i in self.channels:
            self.enabled_commands[i.lower()] = self.default_enables.copy()
            try:
                with open('enabled_commands.txt', 'wb') as f:
                    pickle.dump(self.enabled_commands, f)
            except:
                open('enabled_commands.txt', 'a').close()
                with open('enabled_commands.txt', 'wb') as f:
                    pickle.dump(self.enabled_commands, f)
        