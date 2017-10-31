#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import random

def main(args):
    
    liczba = random.randint(1,10)
    print(liczba)
    for i in range(3):
        odp = int (input ("jaką liczbę mam na myśli? (1,10)"))    
        if liczba == odp:
            print ("zgadłeś!")
        else:
            print ("błąd!")
    
    return 0
    
    

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
