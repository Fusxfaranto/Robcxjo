import pickle

name = 'nickdisable'
enabled = False
operator = True

def cmd(self, c, e, line, message_source, target):
        if len(line[1].split(" ")) < 2:
            self.send(c, target, "Error - Not enough arguments")
        else:
            try:
                if line[1].split(" ", 1)[0].lower() not in self.nickmask_disables:
                    self.nickmask_disables[line[1].split(" ", 1)[0]] = set()
                if line[1].split(" ", 1)[1] not in self.nickmask_disables[line[1].split(" ", 1)[0].lower()]:
                    self.nickmask_disables[line[1].split(" ", 1)[0].lower()].add(line[1].split(" ", 1)[1])
                try:
                    with open('nickmask_disables.txt', 'wb') as f:
                        pickle.dump(self.nickmask_disables, f)
                except:
                    open('nickmask_disables.txt', 'a').close()
                    with open('nickmask_disables.txt', 'wb') as f:
                        pickle.dump(self.nickmask_disables, f)
                    
                self.send(c, target, line[1].split(" ", 1)[1] + " disabled for " + line[1].split(" ", 1)[0])
            except Exception as ex:
                self.send(c, target, "Error: " + str(ex))
            
    