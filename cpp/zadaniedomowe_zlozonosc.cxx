/*
 * zadaniedomowe_zlozonosc.cxx
 */

#include <iostream>
#include <stdio.h>
using namespace std;

int main(int argc, char **argv){

    int n;
    cout <<"podaj liczbe";
    cin >> n;
    int druk = 0;
    
   	for(int i=2;i*i<=n;i++) 
   	{
		if (n%i == 0) 
		{
			cout << "złożona ";
			druk++;
			break;
		}
	}
   	if (not(druk)) cout<<"pierwsza";

    return 0;
}
