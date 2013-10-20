# Searches the echobox for some string
import requests

name = 'echoboxsearch'
enabled = True
operator = False

def cmd(self, c, e, line, message_source, target):
    if len(line) < 2:
        self.send(c, target, u'Error: echoboxsearch needs a term to search')
        return
    with open('echobox.txt', 'r') as f:
        l = f.readlines()
        count = 0
        quotes = []
        for i, d in enumerate([e.arguments[0].split(' ', 1)[1].lower() in s.lower() for s in l]):
            if d:
                quotes.append(l[i])
                count += 1
        if count == 0:
            self.send(c, target, 'No quotes found')
        if count < 4:
            for s in quotes:
                self.send(c, target, u'\u0002Echobox Search: \u000F' + self.eval(c, e, s.replace("\n", ""), target))
        else:
            # This part isn't really going to work for most people.  I chose to handle having a ton of search results
            # by uploading them all to my website.  If you have a host you can do this with, might want to do that,
            # if not, you'll probably need to figure a solution out yourself.
            requests.post('http://fusxfaranto.com/upload.php', files={'file': ('echoboxsearch.txt', ''.join(quotes)), 'password' : self.config['site_password']})
            self.send(c, target, u'Too many search results, see them at http://fusxfaranto.com/uploads/echoboxsearch.txt')