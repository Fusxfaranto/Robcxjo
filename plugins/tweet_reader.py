import twitter, sys

name = 'tweet_reader'
enabled = True
operator = False

def inline(self, c, e, line, message_source, target):
    if "//twitter.com/" in e.arguments[0] and "/status/" in e.arguments[0] and len(e.arguments[0].split("/")) > 5:
        api = twitter.Api(consumer_key=self.config['consumer_key'], consumer_secret=self.config['consumer_secret'], access_token_key=self.config['access_token_key'], access_token_secret=self.config['access_token_secret'])
        try:
            status = api.GetStatus(e.arguments[0].split("/")[5].split(' ')[0])
            self.send(c, target, u'\u0002@' + status.user.screen_name + u' \u000F(' + status.user.name + '): ' + status.text)
        except:
            print "Error: ", sys.exc_info()[0]