#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
 
def zlozonosc(a):
	i = 2
	while not(i>a):
		if a==i:
			print("liczba parzysta")
			return
		i+=2
	print("liczba nieparzysta")

a=int(input("podaj a: "))
while a<0 or a>100:
	print(a)
	a=int(input("podaj a: "))

zlozonosc(a)


