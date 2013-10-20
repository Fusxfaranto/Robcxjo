import goslate

name = 'translate'
enabled = True
operator = False

def cmd(self, c, e, line, message_source, target):
        try:
            if len(line[1]) < 2 or len(line[1].split(" ")) < 2:
                self.send(c, target, u'Error: invalid arguments.  Format:  ,translate from|to thingtotranslate OR ,translate to thingtotranslate')
                return
            gs = goslate.Goslate()
            if len(line[1].split('|')) == 1:
                self.send(c, target, u'\u0002Translate: \u000F' + gs.translate(line[1].split(" ", 1)[1], line[1].split(" ", 1)[0]))
            else:
                self.send(c, target, u'\u0002Translate: \u000F' + gs.translate(line[1].split(" ", 1)[1], line[1].split(" ", 1)[0].split('|')[1], line[1].split(" ", 1)[0].split('|')[0]))
        except:
            self.send(c, target, u'Error translating')
        
    