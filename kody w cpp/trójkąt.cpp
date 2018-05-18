/*
 * trojkat.cpp
 * Program pobiera trzy boki trójkąta,
 * sprawdza, czy da się z nich zbudować trójkąt,
 * oblicza obwód i pole (ze wzoru Herona)
 * i drujuje na ekranie odpowiedni komunikat.
 */


#include <iostream>
#include <cmath>

using namespace std;

int main(int argc, char **argv)
{
    float a, b, c;
    a=b=c=0;
    float p;
    float pole;
    
    cout<<"Podaj długość pierwszego boku: ";
    cin>>a;
    cout<<"Podaj długość drugiego boku: ";
    cin>>b;
    cout<<"Podaj długość trzeciego boku: ";
    cin>>c;
    
    if(a+b>c && a+c>b && b+c>a)
    {
        cout<<"Obwód jest równy: "<<a+b+c<<endl;
        p=(a+b+c)/2;
        pole=sqrt(p*(p-a)*(p-b)*(p-c));
        cout<<"Pole jest równe: " <<pole;
    }
    else
    cout<<"Nie można utworzyć trójkąta";
	return 0;
}
