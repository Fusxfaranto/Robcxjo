name = 'niacki'
enabled = False
operator = False

def inline(self, c, e, line, message_source, target):
    try:
        if self.last_line[target.lower()] == e.arguments[0]:
            self.send(c, target, e.arguments[0] + "niacki")
    except KeyError:
        pass
    self.last_line[target.lower()] = e.arguments[0]