import random

name = 'start'
enabled = True
operator = False

def cmd(self, c, e, line, message_source, target):
        if not message_source == "public" or not self.cah_channel == e.target:
            self.send(c, target, "Error - Need to start a game inside the channel it was created in")
        elif not self.cah_in_progress:
            self.send(c, target, "Error - Game not in session; use ,cardsagainsthumanity to start a new game")
        elif self.cahed:
            self.send(c, target, "Error - Game already started")
        else:
            self.cahed = True
            self.cah_submissions[random.randint(0, len(self.cah_submissions) - 1)] = self.cah_judge_string
            self.cah_black_card = cah_draw(self.cah_black_deck)
            self.cah_black_card_properties = int(self.cah_black_deck_properties.pop(0))
            self.send(c, self.cah_channel, "Judge is " + self.cah_players[self.cah_submissions.index(self.cah_judge_string)])
            s = "Black card"
            if self.cah_black_card_properties == 2:
                s += " (Choose two)"
            elif self.cah_black_card_properties == 3:
                for p in self.cah_players:
                    self.cah_hands[self.cah_players.index(p)].append(cah_draw(self.cah_white_deck))
                    self.cah_hands[self.cah_players.index(p)].append(cah_draw(self.cah_white_deck))
                s += " (Choose three)"
            s += ": " + self.cah_black_card
            self.send(c, self.cah_channel, s)
            self.send(c, self.cah_channel, "Use ,cahhelp for command info")
#                for p in self.cah_players:
#                    for s in self.cah_hands[self.cah_players.index(p)]:
#                        self.send_notice(c, p, "[" + str(self.cah_hands[self.cah_players.index(p)].index(s)) + "] "" + s + """)


def cah_draw(deck):
    card = deck[0]
    deck.pop(0)
    return card.rstrip()
    