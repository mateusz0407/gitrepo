
#include <iostream>

using namespace std;

//int liczba,krok; //zmienne globalne 

int zwieksz ()
{
    int liczba, krok;// zmienne lokalne 
    liczba=liczba + krok;
    return liczba;
}

int main(int argc, char **argv)
{
    int liczba,krok ; //zmienne lokalne
    cout<<"podaj liczbę i krok: ";
    cin>>liczba>>krok;
    
    cout<<"liczba i krok: "<<liczba<<" "<<krok<<endl;
    //zwieksz();
    cout<<"liczba i krok: "<<zwieksz() <<" "<<krok<<endl;
 
         return 0;
}

 
