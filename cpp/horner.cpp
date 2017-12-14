/*
 * horner.cpp
 */
 
#include <iostream>
using namespace std;
float horner(int n, float wsp[20],float x)
{
    if (n==0)
       return wsp[0];
    else
        return horner(n-1, wsp, x)*x+wsp[n];
}

float horner_it(int k, float tbwsp[],float x)
{
    int i;
    float wynik = tbwsp[0];//tbwsp[0]-   0 - pierwsza wartość w tabeli
    for (i=1;i<k+1;i++){
    //k+1 bo bo k to 3 i skończyłoby się na 3 
        wynik = wynik*x + tbwsp[i];
    }
    return wynik;
}

float horner(int n, float wsp[20], float x);
int n=3;
float x,a[20];
int main()
{
    cout<<"Podaj X:  ";
    cin>>x;
    cout<<"Wprowadz wspolczynniki wielomianu: \n";
    for (int i=0;i<=n;i++)
    cin>>a[i];
    cout<<"Wartosc wielomianu =  "<<horner(n,a,x)<<"\n";
    return 0;
}
