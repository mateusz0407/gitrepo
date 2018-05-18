#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  funkcje2.py
#  

def sumuj(x,y):
    return x+y
def odejmij(x,y):
    return x-y

def main(args):
    
    a = int (input("podaj liczbę:"))
    b = int (input("podaj liczbę:"))
    print ("suma:", sumuj(a,b))
    print ("Różnica:", odejmij(a,b))
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
