name = 'raw'
enabled = False
operator = True

def cmd(self, c, e, line, message_source, target):
        self.connection.send(line[1])

    