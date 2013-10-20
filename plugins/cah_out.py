name = 'out'
enabled = True
operator = False

def cmd(self, c, e, line, message_source, target):
        if not message_source == "public" or not self.cah_channel == e.target:
            self.send(c, target, "Error - Need to leave a game inside the channel it was created in")
        elif not e.source.nick in self.cah_players:
            self.send(c, target, "Error - Not in game")
        elif not self.cah_in_progress:
            self.send(c, target, "Error - Game not in session; use ,cardsagainsthumanity to start a new game")
        else:
            index = self.cah_players_old.index(e.source.nick)
            self.cah_players_old.pop(index)
            self.cah_scores_old.pop(index)
            index = self.cah_players.index(e.source.nick)
            self.cah_players.pop(index)
            self.cah_hands.pop(index)
            self.cah_submissions.pop(index)
            self.cah_submissions2.pop(index)
            self.cah_submissions3.pop(index)
            self.cah_scores.pop(index)
            self.send(c, target, e.source.nick + " left the game ;_;")
        
    