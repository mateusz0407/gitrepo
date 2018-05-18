/*
 * tabele.cpp
 */


#include <iostream>

using namespace std ;

void pobierzliczby(int tab[], int ile){
    int i =0;
    for (i=0;i<ile;i++){
            cout<<"podaj liczbę: ";
            cin>>tab[i];}
}
void sumuj (int tab[], int ile){
    int i=0;
    int suma=0;
    for (i=0;i<ile;i++){
        suma+=tab[i];
    }
    cout<<"suma liczb: "<<suma<<endl;
}

void najmniejsza(int tab[], int ile){
    int mini=tab[0];
    int i =0;
    for(i =1; i < mini;i++){
    if(mini >tab[i])
        mini=tab[i];
    }
    cout<<"najmniejsza iczba : "<<mini<<endl;
    }
    
void podzielna(int tab[], int ile){
    int i;
    int licznik=0;
    for (i=0;i<ile;i++){
    if (tab[i] % 5 == 0)
        licznik++;
    }
    cout<<"Podzielnych przez 5: "<< licznik <<endl;
    }


int main(int argc, char **argv)
{
    int rozmiar=0;
    cout<< "ile liczb podasz???";
    cin>>rozmiar;
    int liczby [rozmiar];


    pobierzliczby(liczby,rozmiar);
    sumuj(liczby,rozmiar);
    najmniejsza(liczby, rozmiar);
    podzielna(liczby, rozmiar);
    return 0;
}

