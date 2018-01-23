#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
 
def main(args):
    n = int(input("Podaj liczbe: "))
    i = 2
    while i * i >= n:
        if n % i > 0:
            print("pierwsze")
            break
        i += 1
    while(n % i == 0):
        print("Zlozona")
        break
    return 0
 
 
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
