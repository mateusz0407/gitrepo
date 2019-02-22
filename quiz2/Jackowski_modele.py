#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
from peewee import *


baza_nazwa = "quiz.db"
baza = SqliteDatabase(baza_nazwa)


# MODELE #

class KlasaBaza(Model):
    class Meta:
        database = baza


class Kategoria(KlasaBaza):
    kategoria  = CharField(null=False)
    
class Pytanie(KlasaBaza):
    pytanie = CharField(null=False)
    id_kat = ForeignKeyField(Kategoria, related_name='pytania')

class Odpowiedz(KlasaBaza):
    odpowiedz = CharField(null=False)
    pytanie = ForeignKeyField(pytanie, related_name='odpowiedzi')
    odpok = IntegerField(default = 0)


def main(args):
    if os.path.exists(baza_nazwa):
        os.remove(baza_nazwa)
    baza.connect()  # łączenie z bazą
    baza.create_tables([Kategoria, Pytanie , Odpowiedz])
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
