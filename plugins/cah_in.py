name = 'in'
enabled = True
operator = False

def cmd(self, c, e, line, message_source, target):
        if not message_source == "public" or not self.cah_channel == e.target:
            self.send(c, target, "Error - Need to enter a game inside the channel it was created in")
        elif e.source.nick in self.cah_players:
            self.send(c, target, "Error - Already in game")
        elif not self.cah_progress:
            self.send(c, target, "Error - Game not in session; use ,cardsagainsthumanity to start a new game")
        else:
            self.cah_players.append(e.source.nick)
            self.cah_players_old.append(e.source.nick)
            self.cah_hands.append([])
            for i in xrange(8):
                self.cah_hands[self.cah_players.index(e.source.nick)].append(cah_draw(self.cah_white_deck))
            self.cah_submissions.append(self.cah_unsubmitted_string)
            self.cah_submissions2.append(self.cah_unsubmitted_string)
            self.cah_submissions3.append(self.cah_unsubmitted_string)
            self.cah_scores.append(0)
            self.cah_scores_old.append(0)
            self.send(c, self.cah_channel, e.source.nick + " added to game")
#                self.send_notice(c, e.source.nick, self.cah_get_hand_string(e.source.nick))
        
    
def cah_draw(deck):
    card = deck[0]
    deck.pop(0)
    return card.rstrip()