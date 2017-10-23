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
	for(int i = 0; i < mini;i++){
	if(mini >tab[i])
		mini=tab[i];
	}
	cout<<"najmniejsza iczba : "<<mini<<endl;
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
    return 0;
}

