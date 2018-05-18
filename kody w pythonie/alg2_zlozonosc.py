#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  zlozonosc1.py
#  


def main(args):
    a = 0
    while a < 1 or a > 99:
        a = int(input("podaj liczbę: "))
        #~for i in range(2,  a + 3, 2):
            #~if a == i:
                #~print ("liczba parzysta")
                #~break
        #~if i > a:
            #~print ("liczba nieparzysta")
        
        i = 2
        while i <= a:
            if a == i:
                print("liczba parzysta")
                break
            i += 2
        if i > a:
            print ("liczba nieparzysta")

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
