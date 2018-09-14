#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  funkcje3.py

import random

def wypelnij(lista , ile , maks):
    for i  in range(ile):
        lista.append(random.randint(0, maks))
    return lista


def drukuj(lista):
    licznik =0;
    for liczba in lista:
        if not liczba % 2:
            licznik+=1
    print("liczb parzysta", licznik)


def nieparzyste(lista):
    licznik =0;
    for liczba in lista:
        if liczba % 2:
            licznik+=1
    print("liczb nieparzystych", licznik)


def main(args):
    lista = []
    ile =75
    maks = 100
    wypelnij(lista, ile , maks)
    print(lista)
    drukuj(lista)
    nieparzyste(lista)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
