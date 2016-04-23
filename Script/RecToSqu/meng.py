__author__ = 'GYH'
import sys,os
from PIL import Image

photo = ['.png','.PNG','.jpg','.JPG','.bmp','.BMP','.gif','.GIF']

def Resize(s):
    pic = Image.open(s)
    m,n = pic.size 
    sz = (m+n)/2
    pic_cube = pic.resize((sz,sz))
    pic_cube.save(s[:s.find('.')]+'_square'+s[s.find('.'):])

if __name__ == '__main__':
    path = os.path.abspath('.')
    for s in os.listdir(path):
        if 'square' in s:
            continue
        flag = False
        for c in photo:
            if c in s:
                flag = True
                break
        if flag:
            print s
            Resize(s)
            
