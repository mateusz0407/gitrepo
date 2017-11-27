#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  fibonacci.py
#  

def fib_iter(n):
    """
        Funkcja drukuje kolejne wyrazy ciągu Fibonacciego
        aż do wyrazu n-tego, który zwraca.
        Wersja iteracyjna z pętlą for.
    """
    a, b = 0, 1
    print("wyraz", 1, a)
    print("wyraz", 2, b)
    for i in range(1, n - 1):
        # wynik = a + b
        a, b = b, a + b
        print("wyraz", i + 2, b)

    print()  # wiersz odstępu
    return b


def main(args):
    n = int(input("Podaj nr wyrazu: "))
    fib_iter(n)
    print()
    print("=" * 40)
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
