name = 'judge'
enabled = True
operator = False

def cmd(self, c, e, line, message_source, target):
        if not message_source == "public" or not self.cah_channel == e.target:
            self.send(c, target, "Error - Need to judge inside the channel the game was created in")
        elif not self.cah_in_progress:
            self.send(c, target, "Error - Game not in session; use ,cardsagainsthumanity to start a new game")
        elif not self.cah_started:
            self.send(c, target, "Error - Game hasn't started yet; use ,start to start it")
        elif not e.source.nick == self.cah_players[self.cah_submissions.index(self.cah_string)]:
            self.send(c, target, "Error - Only the judge can judge")
        else:
            try:
                winning_player = self.cah_players[self.cah_submissions.index(self.cah_list_submissions[int(line[1])])]
            except ValueError:
                self.send(c, self.cah_channel, "Error - Not a valid card number")
            except IndexError:
                self.send(c, self.cah_channel, "Error - Not a valid card number")
            else:
                self.cah_judging = False
                self.send(c, self.cah_channel, self.cah_players[self.cah_submissions.index(self.cah_list_submissions[int(line[1])])] + " wins this round!  (Card number " + line[1] + ")")
                
                self.cah_black_deck.append(self.cah_black_card)
                self.cah_black_card = cah_draw(self.cah_black_deck)
                self.cah_black_card_properties = int(self.cah_black_deck_properties.pop(0))
                
                judge_index = self.cah_players_old.index(self.cah_players[self.cah_submissions.index(self.cah_string)]) + 1
                self.cah_submissions = [self.cah_unsubmitted_string] * len(self.cah_submissions)
                self.cah_submissions2 = [self.cah_unsubmitted_string] * len(self.cah_submissions)
                self.cah_submissions3 = [self.cah_unsubmitted_string] * len(self.cah_submissions)
                #self.cah_submissions[random.randint(0, len(self.cah_submissions) - 1)] = self.cah_string
                if judge_index >= len(self.cah_submissions):
                    judge_index = 0
                judge = self.cah_players_old[judge_index]
                
                self.cah_players = self.cah_players_old
                self.cah_scores = self.cah_scores_old
                
                self.cah_submissions[self.cah_players.index(judge)] = self.cah_string
                
                self.cah_scores[self.cah_players.index(winning_player)] += 1
                
                if self.cah_points_to_win in self.cah_scores:
                    self.send(c, self.cah_channel, self.cah_players[self.cah_scores.index(self.cah_points_to_win)] + " wins the game!")
                    self.cah_unsubmitted_string = "seuft5h7"
                    self.cah_string = "uoaygwrg"
                    self.cah_in_progress = False
                    self.cah_started = False
                    self.cah_channel = None
                    self.cah_white_deck = []
                    self.cah_black_deck = []
                    self.cah_black_deck_properties = []
                    self.cah_black_card = None
                    self.cah_black_card_properties = 1
                    self.cah_players = []
                    self.cah_hands = [[]]
                    self.cah_submissions = []
                    self.cah_submissions2 = []
                    self.cah_submissions3 = []
                    self.cah_list_submissions = []
                    self.cah_scores = []
                    self.cah_judging = False
                    self.cah_players_old = []
                    self.cah_scores_old = []
                    self.cah_points_to_win = 8
                
                else:
                    self.send(c, self.cah_channel, "Scores:")
                    for i in xrange(len(self.cah_scores)):
                        self.send(c, self.cah_channel, self.cah_players[i] + ": " + str(self.cah_scores[i]) + " points")
                    
                    self.send(c, self.cah_channel, "Judge is " + self.cah_players[self.cah_submissions.index(self.cah_string)])
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
                    
    
def cah_draw(deck):
    card = deck[0]
    deck.pop(0)
    return card.rstrip()