/*
 * pentle.pp 
 */


#include <iostream>
#include <cstdlib>
using namespace std;

void wypelnij(int tab[] , int ile , int maks){
    srand(time(NULL));
    
    for( int i = 0; i < ile; i++ )
    {
        tab[i] = rand() % maks;
    }
    
    }

void drukuj(int tab[] , int ile){
    int i = 0;
    int licznik = 0;
    for(i = 0; i < ile; i++ )
    {
        cout << tab[i] <<"";
        if (liczba[i] % 2 ==0){
        licznik++ ;
        }
    }
}
int main(int argc, char **argv)
{
    int ile = 75;
    int maks = 200;
    int liczba[ile];
    wypelnij(liczba,  ile, maks); 
    drukuj(liczba, ile)
        
	return 0;
}

