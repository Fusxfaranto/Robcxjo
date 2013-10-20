name = 'cahhelp'
enabled = True
operator = False

def cmd(self, c, e, line, message_source, target):
        self.send_notice(c, e.source.nick, ",cardsagainsthumanity <points to win> -- Initiates a game of Cards Against Humanity")
        self.send_notice(c, e.source.nick, ",in -- Joins the current game")
        self.send_notice(c, e.source.nick, ",out -- Leaves the current game")
        self.send_notice(c, e.source.nick, ",start -- Starts a game, after players have joined")
        self.send_notice(c, e.source.nick, ",hand -- Sends a notice with your current hand")
        self.send_notice(c, e.source.nick, ",pmhand -- Sends a PM with your current hand")
        self.send_notice(c, e.source.nick, ",play <card 1> [card 2] [card 3] -- Submits a card to be judged")
        self.send_notice(c, e.source.nick, ",judge <card number> -- Selects the best card")

    