name = 'print'
enabled = False
operator = True

def cmd(self, c, e, line, message_source, target):
        try:
            exec compile("print " + e.arguments[0].split(" ", 1)[1], '', 'exec')
        except Exception as ex:
            self.send(c, target, "Error: " + str(ex))

    