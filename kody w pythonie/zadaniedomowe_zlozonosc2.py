#!/usr/bin/env python
# -*- coding: utf-8 -*- 

 
def main(args):
    n = int(input("Podaj liczbe: "))
    i = 2
    while n % i > 0:
        if n == 1:
            print("Ani pierwsze ani zlozone")
            break
        if i * i >= n:
            print("pierwsze")
            break
        i += 1
    while(n % i == 0):
        if n == 0:
            print("Ani pierwsze ani zlozone")
            break
        elif n == 2:
            print("Pierwsze")
            break
        print("Zlozona")
        break
    return 0
 
 
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
