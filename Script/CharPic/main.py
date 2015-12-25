#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__="GYH"

from PIL import Image
import argparse

# cmd
parser = argparse.ArgumentParser()

parser.add_argument('file')
parser.add_argument('-o','--output')
parser.add_argument('-wt','--width',type =int,default = 48)
parser.add_argument('-ht','--height',type =int,default = 48)

args = parser.parse_args()

IMG = args.file
WIDTH = args.width
HEIGHT = args.height
OUTPUT = args.output


# char
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

def get_char(r,b,g,alpha = 256):
    if alpha == 0: 
        return ' '
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    unit = (256.0 + 1)/length

    return ascii_char[int(gray/unit)]

if __name__ == '__main__':
    pic = Image.open(IMG)
    pic = pic.resize((WIDTH,HEIGHT),Image.NEAREST)

    out = ""

    for i in range(HEIGHT):
        for j in range(WIDTH):
            out += get_char(*pic.getpixel((j,i)))
        out +='\n'

    print out

    if OUTPUT:
        with open(OUTPUT,'w') as f:
            f.write(out)
    else:
        with open('output.txt','w') as f:
            f.write(out)

