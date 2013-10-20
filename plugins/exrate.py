import requests, json

name = 'exrate'
enabled = True
operator = False

def cmd(self, c, e, line, message_source, target):
        try:
            if len(line[1].split(" ")) < 2:
                self.send(c, target, u'Error: invalid arguments.  Format:  ,exrate from to')
                return
            r = requests.get("http://rate-exchange.appspot.com/currency?from=" + line[1].split(" ")[0] + "&to=" + line[1].split(" ")[1])
            j = json.loads(r.text)
            if 'err' in j:
                self.send(c, target, 'Error converting: ' + j['err'])
            else: 
                self.send(c, target, 'Exchange rate from ' + j['from'].upper() + ' to ' + j['to'].upper() + ': ' + '{0:.4f}'.format(j['rate']))
        except Exception as ex:
            self.send(c, target, "Error converting: " + str(ex))
            
    