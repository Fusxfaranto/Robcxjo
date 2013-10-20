name = 'eggplant'
enabled = False
operator = False


def on_quit(self, c, e):
    try:
        if self.enabled_commands['#taonu']["eggplant"]:
            self.send(c, '#taonu', ".tell " + e.source.nick + " eggplant :)")
            self.send(c, '#taonu', "!tell " + e.source.nick + " eggplant :)")
            self.send(c, '#taonu', "!msg " + e.source.nick + " eggplant :)")
    except KeyError:
        pass