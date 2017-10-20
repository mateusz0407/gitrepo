/*
 * tabele.cpp
 */


#include <iostream>

using namespace std ;

int main(int argc, char **argv)
{
    int liczby [10];
    int i=0;
    int suma=0;
    int parzyste=0;
    for (i=0;i<10;i++){
            cout<<"podaj liczbę: ";
            cin>>liczby[i];
                }
    for (i=0;i<10;i++){

            cout<<liczby [i] <<" ";
            
            suma+=liczby[i];
            if(liczby[i]%2==0)
                parzyste++;
                }
    cout<<"suma liczb: "<<suma<<endl;
    cout<<"ilość liczb parzystych: "<<parzyste<<endl;

    return 0;
}

