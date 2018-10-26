#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  kwerendy.py
import sqlite3

def kwerenda1(cur):
    cur .execute("""
        SELECT nazwisko, imie1 , dzien, miesiac , rok FROM nazwiska
        INNER JOIN dane_osobowe
        ON nazwiska.nr_ucznia=dane_osobowe.nr_ucznia
        WHERE nazwiska.nr_ucznia=(SELECT nr_ucznia FROM nazwiska
        WHERE nazwisko="Gryczon" AND imie1="Agata")
    """)
    
    wynik = cur.fetchall()
    for row in wynik:
        print (tuple(row))
    
        # ~SELECT nazwisko , imie1 , dzien , miesiac, rok FROM nazwiska
        # ~INNER JOIN dane_osobowe ON nazwiska.nr_ucznia=dane_osobowe.nr_ucznia
        # ~WHERE nazwiska.nr_ucznia=9201
    # ~
def main(args):
        ### KONFIGURACJA ###
    baza_nazwa = 'szkola'
    tabele = ['nazwiska', 'dane_osobowe', 'oceny']
    
    con = sqlite3.connect(baza_nazwa + '.db')
    cur = con.cursor()  # obiekt tzw. kursora
    
    kwerenda1(cur)
    
    con.commit()
    con.close()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
