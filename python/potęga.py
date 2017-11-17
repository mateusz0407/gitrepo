#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  potęga.py 
#  

def potega_it(x,n):
    i = 1
    wynik = 1
    while i <= n:
        wynik = wynik *x
        i = i + 1
    return wynik
    
def main (args):
    x = float(input("Podaj podstawę: "))
    n = int(input("Podaj wykładnik: "))
    assert potega(1,1) == 1
    assert potega(2,1) == 2
    assert potega(3,3) == 27
    assert potega(2,2) == 4
    
    
    print ("wynik:" , potega(x,n))
    return 0
    
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
