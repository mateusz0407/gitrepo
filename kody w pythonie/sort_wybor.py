import random

tab=[]
for i in range(6):
    tab.append(random.randrange(6))
print(tab)


def wybieranie(tab):
    for i in range(6):
        mn=tab[i]
        mini=i
        for j in range(i,6):
            if (mn>tab[j]):
                mn=tab[j]
                mini=j
        tab[i],tab[mini]=tab[mini],tab[i]
    return tab

print (wybieranie(tab))
