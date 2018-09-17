/*
 * pentle.pp 
 */


#include <iostream>
#include <cstdlib>
using namespace std;
void wypelnij(int tab[], int ile, int maks){
    srand(time(NULL));
    int i = 0;
    for (i = 0; i < ile; i++)
    {
        tab[i] = rand() % maks;
        }
}
void drukuj(int tab[], int ile){
    int i = 0;
    int licznik = 0;
    for (i = 0; i < ile; i++)
    {
        cout << tab[i] << " ";
        if(tab[i]%2 == 0) {
            
            licznik++;
            }
        
        }
    cout << endl;
    cout << "Liczb nie parzystych " << licznik << endl;
    
}
void nieparzyste (int tab[], int ile)
{
	int suma = 0;
	for (int i = 0; i < ile; i++)
	{
		if (tab[i] % 2 != 0)
		{
			suma = suma + tab[i];
			cout << tab[i] << endl;
		}
	}
	cout << "Suma liczb nieparzystych: " << suma << endl;
}
int main(int argc, char **argv)
{
    
    int ile = 75;
    int maks = 200;
	int liczby[ile];
    
    wypelnij(liczby, ile, maks);
    drukuj(liczby,ile);   
    nieparzyste(liczby, ile);
  
    
	return 0;
}
