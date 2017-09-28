/*
 * hello.cpp

 */


#include <iostream>
using namespace std;


int main(int argc, char **argv)
{
 //char imie; // deklaracja zminnej znakowej 
 char imie[10]; // deklaracja zminnej tablicowej  
 int wiek;
 wiek = 0; //inicjacja zmiennej

	cout << "Witaj w C++!!" << endl;
	cout << "Podaj imie: ";
	//cin >> imie;
    cin.getline (imie, 10);
    cout << "cześć, " << imie << "!" << endl;
    cin.ignore();
    cout << "ile masz lat??? ";
    cin >> wiek;
    cout << "urodziłeś się w " << 2017 - wiek << endl;
    return 0;
}

