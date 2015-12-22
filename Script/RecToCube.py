import sys
from PIL import Image

photo = ['.png','.jpg','.bmp','.gif','.psd','.jpeg']

def Resize(s):
    pic = Image.open(s)
    m,n = pic.size 
    sz = (m+n)/2
    pic_cube = pic.resize((sz,sz))
    pic_cube.save(s[:s.find('.')]+'_cube'+s[s.find('.'):])

if __name__ == '__main__':
    for s in sys.argv[1:]:
        flag = False
        for c in photo:
            if c in s:
                flag = True
                break
        if flag:
            print s
            Resize(s)
            
