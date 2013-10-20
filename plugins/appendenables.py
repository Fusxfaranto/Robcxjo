import pickle

name = 'appendenables'
enabled = False
operator = True

def cmd(self, c, e, line, message_source, target):
        for i, d in self.enabled_commands.iteritems():
            for f in self.default_enables:
                if not f in d:
                    self.enabled_commands[i][f] = self.default_enables[f]
            try:
                with open('enabled_commands.txt', 'wb') as f:
                    pickle.dump(self.enabled_commands, f)
            except:
                open('enabled_commands.txt', 'a').close()
                with open('enabled_commands.txt', 'wb') as f:
                    pickle.dump(self.enabled_commands, f)
                    
    