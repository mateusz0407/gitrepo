#!/usr/bin/env python
# -*- coding: utf-8 -*-


def szyfruj_cezara(tekst, klucz):
    klucz = klucz % 26
    szyfrogram = " "
    for znak in tekst:
        znak = znak.upper()
        ascii = ord(znak) + klucz
        if ascii > 90:
            ascii -= 26
        szyfrogram += chr(ascii)
    return szyfrogram


def main(args):
    tekst = input("podaj tekst: ")
    klucz = int(input("klucz: "))

    szyfrogram = szyfruj_cezara(tekst, klucz)
    print(szyfrogram)
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
