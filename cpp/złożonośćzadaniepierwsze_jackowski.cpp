/*
 * złożonośćzadaniepierwsze_jackowski.cpp
 */


#include <iostream>
using namespace std;
int main(int argc, char **argv)
{
	int a ;
	while(a >100 || a < 0){
		cout<<"podaj liczbę: "<<endl;
		cin>>a;
	}
	for(int i = 2; i !=a; i += 2){
		if(i == 100)
			cout<< a <<"liczba jest nieparzysta "<< endl;
		}
		cout<< a <<"liczba jest parzysta "<<endl;
	return 0;
}
