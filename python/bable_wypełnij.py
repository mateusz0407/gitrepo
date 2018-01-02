#!/usr/bin/env python
# -*- coding: utf-8 -*-

def wstaw(lista):
    for i in range(1,len(lista)):
        el = lista[i]
        j = i - 1
        while j>=0 and lista[j]<el:# wyszukiwanie pozycji
            lista[j + 1] = lista[j]# przesuwanie elementów
            j = j - 1
        lista[j + 1] = el
    return lista

        
def main(args):
    lista = [3, 4, 7, 0, 2, 3, 1, 9]
    print(lista)
    print(wstaw(lista))
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
