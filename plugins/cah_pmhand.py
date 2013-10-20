import irc

name = 'pmhand'
enabled = True
operator = False

def cmd(self, c, e, line, message_source, target):
        if not e.source.nick in self.cah_players:
            self.send(c, target, "Error - Need to be in a game to view your hand")
        elif self.cah_judging:
            self.send(c, e.source.nick, "Sorry, viewing your hand during judging doesn't work")
        else:
            hand = ""
            for s in self.cah_hands[self.cah_players.index(e.source.nick)]:
                hand += "[" + str(self.cah_hands[self.cah_players.index(e.source.nick)].index(s)) + "] \"" + s + "\" "
            try:
                self.send(c, e.source.nick, hand)
            except irc.client.MessageTooLong:
                print "message too long"