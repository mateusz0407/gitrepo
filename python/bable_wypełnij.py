#!/usr/bin/env python
# -*- coding: utf-8 -*-

def sort_wstaw_max(lista):
    """wersja liniowa"""
    for i in range(1, len(lista)):
        el = lista[i]
        k = i - 1
        while k >= 0 and lista[k] > el:  # wyszukuje pozycje do wstawienia
            lista[k + 1] = lista[k]  # przesowanie w gore tabeli
            k -= 1
        lista[k + 1] = el  # wstawienie elementu
    return lista


def sort_wstaw_min(lista):
    """wersja liniowa"""
    for i in range(1, len(lista)):
        el = lista[i]
        k = i - 1
        while k >= 0 and lista[k] < el:  # wyszukuje pozycje do wstawienia
            lista[k + 1] = lista[k]  # przesowanie w gore tabeli
            k -= 1
        lista[k + 1] = el  # wstawienie elementu
    return lista


def main(args):
    lista = [4, 3, 7, 0, 2, 3, 1, 9]
    # [3, 4, 7, 0, 2, 3, 1, 9]
    # [3, 4, 7, 0, 2, 3, 1, 9]
    # [0, 3, 4, 7, 2, 3, 1, 9]

    print(lista)
    print("Posortowana lista od najwiekszej: ", sort_wstaw_max(lista))
    print("Posortowana lista od najmniejszek: ", sort_wstaw_min(lista))

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
