import random

name = 'cardsagainsthumanity'
enabled = False
operator = False

def cmd(self, c, e, line, message_source, target):
        if self.cah_in_progress:
            self.send(c, target, "Error - Game already in progress")
        elif not message_source == "public":
            self.send(c, target, "Error - Game must be started in a channel")
        elif len(line) < 2:
            self.send(c, target, "Error - Not enough arguments")
        else:
            self.send(c, target, u'\u0002Starting game of Cards Against Humanity!  Type ,in to join!\u000F')
            
            self.cah_channel = target
            self.cah_in_progress = True
            self.cah_started = False
            self.cah_players = []
            self.cah_scores = []
            self.cah_judging = False
            deck = file("whitedeck.txt", "r")
            self.cah_white_deck = deck.readlines()
            deck.close()
            deck = file("blackdeck.txt", "r")
            self.cah_black_deck = deck.readlines()
            deck.close()
            deck = file("blackdeckproperties.txt", "r")
            self.cah_black_deck_properties = deck.readlines()
            deck.close()
            
            self.cah_points_to_win = int(line[1])
            
            indexes = range(len(self.cah_black_deck))
            random.shuffle(indexes)
            temp_a, temp_b = [], []
            for i in indexes:
                temp_a.append(self.cah_black_deck[i])
                temp_b.append(self.cah_black_deck_properties[i])
            self.cah_black_deck = temp_a
            self.cah_black_deck_properties = temp_b
            random.shuffle(self.cah_white_deck)
            
def init(self):
    self.cah_unsubmitted_string = "seuft5h7"
    self.cah_judge_string = "uoaygwrg"
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