#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

def losuj(ileliczb,maksliczby):
    liczby = [] #pusta lista

    ile = 0 #liczba unikalnych liczb
    #for i in range (ileliczb):
    while ile < ileliczb:
        liczba = random.randint(0 , maksliczby)
        if liczby.count(liczba)==0:
                liczby.append(liczba)
                ile +=1
    print(liczby)
    return liczby

def main(args):
    ileliczb = int(input ("ile liczb chce zgadywac?"))
    maksliczby = int(input ("maksymalna losowana liczba: "))

    liczby = losuj(ileliczb , maksliczby)

    #pobieraie typów użytkownika
    typy = set() # pusty zbiór
    for i in random(ileliczb):
        typ = input("podaj typ: ")
        typy.add(typ)

    print(typy)
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
