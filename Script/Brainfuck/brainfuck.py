#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__="GYH"

import sys

ST = [0]
nex = lst = ptr = it = 0
lens = len(ST)

def Compile(floor):
    global nex,lst,ptr,it,lens,ST
    while it < len(S):
        ch = S[it]
        #print it,floor,ptr,ST[ptr],ch,"-=-"
        if ch == '<':
            ptr -= 1
        elif ch == '>':
            ptr += 1
            if ptr == lens:
                lens += 1
                ST.append(0)
        elif ch == '+': ST[ptr] += 1
        elif ch == '-': ST[ptr] -= 1
        elif ch == '.': sys.stdout.write(chr(ST[ptr]))
        elif ch == ',': 
            s = raw_input()
            if s=='': s = '\n'
            print ord(s)
            ST[ptr] = ord(s)
        elif ch == '[': 
            lst = it
            it += 1
            it = Compile(floor+1)
        elif ch == ']':
            if ST[ptr]: return lst-1
            else: return it
        it += 1
    return it

if __name__ == '__main__':
    #try:
        F = open(sys.argv[1])
        S = F.read()
        S = ''.join(S.split())
        if Compile(0) >= len(S):
            print
            print 22*'-'
            print
            print "Compile OK"
    #except BaseException,e:
    #    print e

