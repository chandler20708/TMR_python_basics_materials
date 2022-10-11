from urllib.request import urlopen
from PIL import Image
def showimg(img = 'https://i.imgur.com/cEycfN7.png'):
    img =Image.open(open(img, 'rb'))
    img.show()

def show(img = 'https://i.imgur.com/cEycfN7.png'):
    img = Image.open(urlopen(img))
    img.show()