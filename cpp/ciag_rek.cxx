/*
 * ciag_rek.cxx
 */


#include <iostream>
 
using namespace std;
 
//a1 = 2
//an = an-1 * n^2 - 1
 
int wyraz(int n)
{
    if(n==1)
        return 2;
    return wyraz(n -1) * wyraz(n * n) + 1;
}
 
int main()
{
    int n=0;
    cout<<"Podaj n: ";
    cin>>n;
    
    cout<<wyraz(n)<<endl;
    return 0;
}
