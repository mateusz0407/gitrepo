#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  bmi.py
#  
#  Copyright 2018 Dell <Dell@DESKTOP-PF62GF8>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  


def main(args):
	height = float(input("podaj wzrost(w metrach): "))
	weight = int(input("Podaj wagé(w kilogramach): "))
	bmi = round(weight/ (height * height), 1)

	if bmi <= 18.5:
		print('Twoje BMI wynosi: ', bmi, 'masz niedowagę')

	elif bmi > 18.5 and bmi < 25:
		print('Twoje BMI wynosi: ', bmi, 'jesteß w optymalnym stanie ')

	elif bmi > 25 and bmi < 30:
		print('Twoje BMI wynosi: ', bmi, "masz nadwagé")

	elif bmi > 30:
		print('Twoje BMI wynosi: ', bmi, "jestes otyly")

	else:
		print('Blads')
    
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
