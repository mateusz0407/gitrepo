/*
 * bmi.cpp
 */

#include <iostream>

using namespace std;

int main()
{
    float waga ,  wzrost , bmi ;
    cout << "Podaj swoja wage: " << endl;
    cin >> waga; cout << endl;
    cout << "Podaj swoj wzrost(w metrach): " << endl;
    cin >> wzrost; cout << endl;
    bmi = waga /( wzrost * wzrost );
    cout << "Twoje bmi wynosi: " << bmi << endl;
    cout << "w jakim satnie jesteś" << endl;
    if( bmi <= 18.5 )
         cout << "Masz niedowagę!!!" << endl;
    
    if( bmi > 18.5 && bmi <= 25 )
         cout << "Twoja waga jest optymalna !!!" << endl;
    
    if( bmi > 25 && bmi <= 30 )
         cout << "Masz otyłość!!!" << endl;
    
    if( bmi > 30 )
         cout << "Jesteś otyły!!!" << endl;
    
    return 0;
}
