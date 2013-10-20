import random

name = 'play'
enabled = True
operator = False

def cmd(self, c, e, line, message_source, target):
        if not message_source == "public" or not self.cah_channel == e.target:
            self.send(c, target, "Error - Need to play inside the channel the game was created in")
        elif not self.cah_in_progress:
            self.send(c, target, "Error - Game not in session; use ,cardsagainsthumanity to start a new game")
        elif not self.cah_started:
            self.send(c, target, "Error - Game hasn't started yet; use ,start to start it")
        elif self.cah_submissions[self.cahers.index(e.source.nick)] == self.cah_judge_string:
            self.send(c, target, "Error - The judge can't submit a card")
        elif not e.source.nick in self.cahers:
            self.send(c, target, "Error - Need to be in game to play a card")
        elif not self.cah_submissions[self.cahers.index(e.source.nick)] == self.cah_unsubmitted_string:
            self.send(c, target, "Error - Already submitted card(s)")
        elif len(line[1].split(" ")) != 2 and self.cah_black_card_properties == 2:
            self.send(c, target, "Error - Invalid number of cards")
        elif len(line[1].split(" ")) != 3 and self.cah_black_card_properties == 3:
            self.send(c, target, "Error - Invalid number of cards")
        elif self.cah_judging:
            self.send(c, target, "Error - Cards are being judged, can't submit")
#            elif self.cah_black_card_properties > 2 and self.cah_submissions3[self.cahers.index(e.source.nick)] == self.cah_unsubmitted_string:
#                try:
#                    self.cah_submissions3[self.cahers.index(e.source.nick)] = self.cah_hands[self.cahers.index(e.source.nick)][int(line[1])]
#                except ValueError:
#                    self.send(c, self.cah_channel, "Error - Not a valid card number")
#                except IndexError:
#                    self.send(c, self.cah_channel, "Error - Not a valid card number")
#                else:
#                    self.cah_white_deck.append(self.cah_hands[self.cahers.index(e.source.nick)].pop(int(line[1])))
#           elif self.cah_black_card_properties > 1 and self.cah_submissions2[self.cahers.index(e.source.nick)] == self.cah_unsubmitted_string:
#                try:
#                    self.cah_submissions2[self.cahers.index(e.source.nick)] = self.cah_hands[self.cahers.index(e.source.nick)][int(line[1])]
#                except ValueError:
#                    self.send(c, self.cah_channel, "Error - Not a valid card number")
#                except IndexError:
#                    self.send(c, self.cah_channel, "Error - Not a valid card number")
#                else:
#                    self.cah_white_deck.append(self.cah_hands[self.cahers.index(e.source.nick)].pop(int(line[1])))
        else:
            try:
                if len(line[1].split(" ")) == 3:
                    self.cah_submissions3[self.cahers.index(e.source.nick)] = self.cah_hands[self.cahers.index(e.source.nick)][int(line[1].split(" ")[0])]
                    self.cah_submissions2[self.cahers.index(e.source.nick)] = self.cah_hands[self.cahers.index(e.source.nick)][int(line[1].split(" ")[1])]
                    self.cah_submissions[self.cahers.index(e.source.nick)] = self.cah_hands[self.cahers.index(e.source.nick)][int(line[1].split(" ")[2])]
                elif len(line[1].split(" ")) == 2:
                    self.cah_submissions2[self.cahers.index(e.source.nick)] = self.cah_hands[self.cahers.index(e.source.nick)][int(line[1].split(" ")[0])]
                    self.cah_submissions[self.cahers.index(e.source.nick)] = self.cah_hands[self.cahers.index(e.source.nick)][int(line[1].split(" ")[1])]
                else:
                    self.cah_submissions[self.cahers.index(e.source.nick)] = self.cah_hands[self.cahers.index(e.source.nick)][int(line[1].split(" ")[0])]
            except ValueError:
                self.send(c, self.cah_channel, "Error - Not a valid card number")
            except IndexError:
                self.send(c, self.cah_channel, "Error - Not a valid card number")
            else:
                if self.cah_black_card_properties > 2:
                    self.cah_white_deck.append(self.cah_hands[self.cahers.index(e.source.nick)].pop(self.cah_hands[self.cahers.index(e.source.nick)].index(self.cah_submissions3[self.cahers.index(e.source.nick)])))
                if self.cah_black_card_properties > 1:
                    self.cah_white_deck.append(self.cah_hands[self.cahers.index(e.source.nick)].pop(self.cah_hands[self.cahers.index(e.source.nick)].index(self.cah_submissions2[self.cahers.index(e.source.nick)])))
                self.cah_white_deck.append(self.cah_hands[self.cahers.index(e.source.nick)].pop(self.cah_hands[self.cahers.index(e.source.nick)].index(self.cah_submissions[self.cahers.index(e.source.nick)])))
#                    self.cah_white_deck.append(self.cah_hands[self.cahers.index(e.source.nick)].pop(int(line[1].split(" ")[0])))
                self.cah_hands[self.cahers.index(e.source.nick)].append(cah_draw(self.cah_white_deck))
                if self.cah_black_card_properties == 2:
                    self.cah_hands[self.cahers.index(e.source.nick)].append(cah_draw(self.cah_white_deck)) #make it message new cards, also instead of poppin change submitted card
#                    self.send_notice(c, e.source.nick, self.cah_get_hand_string(e.source.nick))
                if not self.cah_unsubmitted_string in self.cah_submissions:
                    self.cah_judging = True
                    s = "Black card"
                    if self.cah_black_card_properties == 2:
                        s += " (Choose two)"
                    elif self.cah_black_card_properties == 3:
                        s += " (Choose three)"
                    s += ": " + self.cah_black_card
                    self.send(c, self.cah_channel, s)
                    
                    self.cahers_old = self.cahers
                    self.cah_scores_old = self.cah_scores
                    
                    indexes = range(len(self.cahers))
                    random.shuffle(indexes)
                    temp_a, temp_b, temp_c, temp_d, temp_e = [], [], [], [], []
                    for i in indexes:
                        temp_a.append(self.cahers[i])
                        temp_b.append(self.cah_submissions[i])
                        temp_c.append(self.cah_scores[i])
                        temp_d.append(self.cah_submissions2[i])
                        temp_e.append(self.cah_submissions3[i])
                    self.cahers = temp_a
                    self.cah_submissions = temp_b
                    self.cah_scores = temp_c
                    self.cah_list_submissions = []
                    self.cah_submissions2 = temp_d
                    self.cah_submissions3 = temp_e
                    for s in self.cah_submissions:
                        if not s == self.cah_judge_string:
                            self.cah_list_submissions.append(s)
                    for s in self.cah_list_submissions:
                        if self.cah_black_card_properties > 2:
                            self.send(c, self.cah_channel, "[" + str(self.cah_list_submissions.index(s)) + "] " + self.cah_submissions3[self.cah_submissions.index(s)])
                        if self.cah_black_card_properties > 1:
                            self.send(c, self.cah_channel, "[" + str(self.cah_list_submissions.index(s)) + "] " + self.cah_submissions2[self.cah_submissions.index(s)])
                        self.send(c, self.cah_channel, "[" + str(self.cah_list_submissions.index(s)) + "] " + s)
                        
                        
def cah_draw(deck):
    card = deck[0]
    deck.pop(0)
    return card.rstrip()