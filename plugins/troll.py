from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
import textwrap
import requests

enabled = True
operator = False
name = 'troll'
        
def cmd(self, c, e, line, message_source, target):
    if len(line) < 2:
        self.send(c, target, "troll: http://fusxfaranto.com/uploads/troll.png")
        return
    img = Image.open("trollbase.png")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("/usr/share/fonts/truetype/msttcorefonts/Courier_New_Bold.ttf", 16)
    text = self.troll_wrapper.wrap(line[1])
    #text = textwrap.TextWrapper(width=34).wrap(line[1])
    
    #while len(text[-1]) > 34:
    #    text.append(text[-1][34:])
    #    text[-2] = text[-2][:34]
        
    for i in xrange(0, len(text)):
        draw.text((2, 2 + i * 16),text[i],(0, 0, 0),font=font)
        
    img.save('troll.png')
    r = requests.post('http://fusxfaranto.com/upload.php', files={'file' : open('troll.png', 'rb'), 'password' : self.config['site_password']})
    print r.text
    
    self.send(c, target, "troll: http://fusxfaranto.com/uploads/troll.png")

def init(self):
    self.troll_wrapper = textwrap.TextWrapper(width=34)