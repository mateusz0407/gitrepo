/*
 * potęga.cpp
 * a0 = 1
 * a1 = a
 * an = a*...*a (n-czynników) dla n zaw.N+ - {1}
 */


#include <iostream>

using namespace std;

float potega_it(float x, int n){
    float wynik = 1;
    for(int i=0;i<n;i++){
        cout<< i <<endl;
        wynik = wynik*x;
    }
    return wynik;
}

int main(int argc, char **argv)
{
    //pobierz od użytkownika podstawę i wykładnik
    float x = 0;
    int n = 0;
    cout<<"podaj podstawę"<<endl;
    cin>>x;
    cout<<"podaj wykładnik"<<endl;
    cin>>n;
    cout<<"potęga: "<<potega_it(x,n)<<endl;
        
    return 0;
}

