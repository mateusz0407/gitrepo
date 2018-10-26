#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  kwerendy.py
import sqlite3

def kwerenda1(cur):
    cur .execute("""
        SELECT klasa , COUNT(nazwisko) AS ilu FROM klasy
        INNER JOIN uczniowie ON klasy.id=uczniowie.id_klasa
        GROUP BY klasa
        ORDER BY ilu DESC
    """)
    # ~SELECT klasa , COUNT(nazwisko) FROM klasy
    wynik = cur.fetchall()
    for row in wynik:
        print (tuple(row))
    
        # ~SELECT nazwisko , imie1 , dzien , miesiac, rok FROM nazwiska
        # ~INNER JOIN dane_osobowe ON nazwiska.nr_ucznia=dane_osobowe.nr_ucznia
        # ~WHERE nazwiska.nr_ucznia=9201
    # ~
def main(args):
        ### KONFIGURACJA ###
    baza_nazwa = 'uczniowie'
    tabele = ['uczniowie', 'klasy', 'przedmioty', 'oceny']
    
    con = sqlite3.connect(baza_nazwa + '.db')
    cur = con.cursor()  # obiekt tzw. kursora
    
    kwerenda1(cur)
    
    con.commit()
    con.close()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))


# ~WHERE nazwiska.nr_ucznia=(SELECT nr_ucznia FROM nazwiska
        # ~WHERE nazwisko="German" AND imie1="Dariusz")
