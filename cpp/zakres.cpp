
#include <iostream>

using namespace std;

//int liczba,krok; //zmienne globalne 

int zwieksz (int liczba,int krok)
{
    liczba=liczba + krok;
    krok=3*krok;
    return krok;
}

void zwieksz2(int &a,int &b){
    a=a+b;
    b=3*b;
    }

int main(int argc, char **argv)
{
    int liczba,krok ; //zmienne lokalne
    cout<<"podaj liczbę i krok: ";
    cin>>liczba>>krok;
    
    cout<<"liczba i krok: "<<liczba<<" "<<&liczba<<endl;
    /*zwieksz2(liczba, krok);
    cout<<"liczba i krok: "<<" "<<krok<<endl;
    */
         return 0;
}

 
