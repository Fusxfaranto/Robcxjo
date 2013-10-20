name = 'exec'
enabled = False
operator = True

def cmd(self, c, e, line, message_source, target):
        try:
            if line[1] == "block":
                exec compile(self.block_text, '', 'exec')
            else:
                exec compile(e.arguments[0].split(" ", 1)[1], '', 'exec')
                self.send(c, target, "Done")
        except Exception as ex:
            self.send(c, target, "Error: " + str(ex))
    
    