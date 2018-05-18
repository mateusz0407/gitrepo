#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  sumuj 2.py
#

def main(args):
    suma = 0
    ile = 0
    while True:
        liczba = int (input("podaj liczbę:"))
        suma=suma+liczba
        ile=ile+1
        if suma > 100:
            break
    print("wprowadzono", ile ,"liczb.")
    print("suma;", suma)
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
