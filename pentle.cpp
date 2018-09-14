/*
 * pentle.pp 
 */


#include <iostream>
#include <cstdlib>
using namespace std;
int main(int argc, char **argv)
{
    int liczba[50];
    int i = 0;
    srand(time(NULL));
    int licznik = 0;
    
    for( i = 0; i < 50; i++ )
    {
        liczba[i] = rand() % 100;
    }
    for( i = 0; i < 50; i++ )
    {
        cout << liczba[i] <<endl;
        {
        if (liczba[i] % 2 ==0)
        licznik++ ;
        }
    }
    cout << "Parzyste elementy tabeli: " <<licznik<<endl;

	return 0;
}

