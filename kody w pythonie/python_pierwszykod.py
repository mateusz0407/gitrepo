#!/usr/bin/env python
# -*- coding: utf-8 -*-



# osoba = "Mateusz Jackowski"
#osoba = 'Mateusz Jackowski'
osoba = input("jak się nazywasz??")
wiek = input("ile masz lat ??")
print ("Witaj" , osoba, "!")
print ("Urodziłeś sie", 2017-int(wiek))
rok_phytona = 1991
wiek_phytona = 2017-rok_phytona
if wiek_phytona>int(wiek):
    print ("jestem starszy!")
elif wiek_phytona<int(wiek):
    print ("jestem młodszy!")
else:
    print ("Mamy tyle samo lat")
