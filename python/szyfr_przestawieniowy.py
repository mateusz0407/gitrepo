#!/usr/bin/env python
# -*- coding: utf-8 -*-


def szyfruj(tekst, klucz):
    reszta = len(tekst) % klucz
    if reszta:
        tekst += reszta * (klucz - reszta) * "."

    szyfrogram = ""
    for i in range(klucz):
        for j in range(int(len(tekst) / klucz)):
            szyfrogram += tekst[i]

    return szyfrogram


def main(args):
    tekst = input("podaj tekst: ")
    klucz = int(input("klucz: "))
    while 2 * klucz > len(tekst):
        klucz = int(input("klucz: "))
    szyfrogram = szyfruj(tekst, klucz)
    print(szyfrogram)
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
