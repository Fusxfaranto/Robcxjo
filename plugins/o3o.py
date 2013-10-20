from time import sleep

name = 'o3o'
enabled = False
operator = False

def inline(self, c, e, line, message_source, target):
    if "o3o" in e.arguments[0]:
        if self.o3o_counter < 5 and self.o3o_counter >= 0:
            self.send(c, target, "o3o")
            self.o3o_counter += 1
        elif self.o3o_counter >= 5:
            sleep(3)
    else:
        self.o3o_counter = 0
        

def init(self):
    self.o3o_counter = 0