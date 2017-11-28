#!/usr/bin/env python
# -*- coding: utf-8 -*-


def fib_iter(n):
    """
        Funkcja drukuje kolejne wyrazy ciągu Fibonacciego
        aż do wyrazu n-tego, który zwraca.
        Wersja iteracyjna z pętlą for.
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    print(a)
    print(b)
    for i in range(1, n):
        # wynik = a + b
        tmp = b
        b = a + b
        a = tmp
        print(a, " ", b)

    print()  # wiersz odstępu
    return b


def main(args):
    # n = int(input("Podaj nr wyrazu: "))
    print("wyraz {:d} = {:d}".format(10, fib_iter(10)))
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
