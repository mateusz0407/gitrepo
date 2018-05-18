#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random


def losuj(ileliczb, maksliczb):
    liczby = []  # pusta lista

    ile = 0  # liczba unikalnych liczb
    # for i in range (ileliczb):

    while ile < ileliczb:
        liczba = random.randint(0, maksliczb)
        if liczby.count(liczba) == 0:
                liczby.append(liczba)
                ile += 1

    return liczby


def pobierz_typy(ileliczb):
    # pobieraie typów użytkownika
    typy = set()  # pusty zbiór
    # for i in random(ileliczb):
    ile = 0
    while ile < ileliczb:
        typ = int(input("podaj typ: "))
        if typ not in typy:
            typy.add(typ)
            ile += 1

    return typy


def main(args):
    ileliczb = int(input("ile liczb chce zgadywac?"))
    maksliczb = int(input("maksymalna losowana liczba: "))

    while ileliczb > maksliczb or ileliczb < 1:
        ileliczb = int(input('ile liczb chce zgadnąć z %s' % maksliczb))

    liczby = losuj(ileliczb, maksliczb)
    typy = pobierz_typy(ileliczb)

    trafione = set(liczby) & typy
    print(trafione)

    print ("trafiłeś", len(trafione), "liczby.")

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
