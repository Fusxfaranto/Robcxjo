from time import strftime

name = 'highlightpm'
enabled = True
operator = False

def inline(self, c, e, line, message_source, target):
    if ("fusx" in e.arguments[0].lower() or "fawful" in e.arguments[0].lower()) and not e.source.nick == "TIBot" and not e.source.nick == "FUCKUIMABOT" and not e.source.nick == "Fusxfaranto" and not e.source.nick == "skybot" and not e.source.nick == "Robcxjo":
        self.send(c, "Fusxfaranto", "Highlight in " + e.target + " | [" + strftime("%H:%M:%S") + "] <" + e.source.nick + "> " + e.arguments[0])