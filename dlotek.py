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
    print(liczby)
    return liczby


def main(args):
    ileliczb = int(input("ile liczb chce zgadywac?"))
    maksliczb = int(input("maksymalna losowana liczba: "))

    liczby = losuj(ileliczb, maksliczb)

    # pobieraie typów użytkownika
    typy = set()  # pusty zbiór
    # for i in random(ileliczb):
    ile = 0
    while ile < ileliczb:
        typ = input("podaj typ: ")
        if typ not in typy:
            typy.add(typ)
            ile += 1
    print(typy)
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
