#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  potęga2.py
#  

def potega_it(a,b):
	
	i = 1 
	wynik = 1
	while i <= b :
		wynik = wynik * a
		i = i+1
	
	return wynik
    

def main(args):
	a = float(input("Podaj podstawę"))
	b = int(input("Podaj wykładnik"))
	print ("wynik: ", potega_it(a,b))
	
	
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
