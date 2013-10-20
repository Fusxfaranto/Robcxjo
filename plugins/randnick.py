import random

name = 'randnick'
enabled = True
operator = False

def evaluator(self, c, e, s, target):
    try:
        s = ''.join(s).replace("$RANDNICK", ''.join(random.choice(self.users_in_channel[e.target.lower()])).replace("~", "").replace("&", "").replace("@", "").replace("%", "").replace("+", ""), 1)
        
        while "$RANDNICK" in s:
            s = s.replace("$RANDNICK", random.choice(self.users_in_channel[e.target.lower()]).replace("~", "").replace("&", "").replace("@", "").replace("%", "").replace("+", ""), 1)
    except KeyError:
        c.send_raw("NAMES " + target)
        
    return s