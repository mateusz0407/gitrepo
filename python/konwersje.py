#!/usr/bin/env python
# -*- coding: utf-8 -*-


def konwersja1(liczba10, podstawa):
    """
    funkcja zamienia liczbę dziesietna na system o podanekj podstawie
    """
    liczba = []  # lista reszt
    while liczba10 != 0:
        reszta = liczba10 % podstawa
        if reszta > 9:
            reszta = chr(reszta + 55)
        liczba.append(str(reszta))
        liczba10 = int(liczba10 / podstawa)

    liczba.reverse()  # odwrócenie kolejności
    return "".join(liczba)  # złączenie elemetów listy w ciąg


def dec2other():
    """
    funkcja zamienia liczbę dziesietna na system o podanekj podstawie
    """
    liczba = int(input("podaj liczbę: "))
    podstawa = int(input("podaj podstawe: "))
    while podstawa < 2 or podstawa > 16:
        podstawa = int(input("podaj podstawe: "))
    print("wynik konwersji: {}(10)={}({})".format(
        liczba, konwersja1(liczba, podstawa), podstawa))


def konwersja2(liczba, podstawa):
	suma = 0
	for i in range(len(liczba)-1):
		suma+=int(liczba[i])
		suma*=podstawa
	suma+=int(liczba[i + 1])
	return suma


def other2dec():
    system = int(input("podaj system: "))
    licz = input("podaj liczbę: ")
    print(konwersja2(licz, system))


def main(args):
    print("zmiana liczby dziesiatną na liczbe o podajej podstawie"
          "<2;16> lub odwrotnie")
    dec2other()
    other2dec()
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
