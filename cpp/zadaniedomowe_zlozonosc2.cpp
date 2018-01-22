/*
 * zadaniedomowe_zlozonosc2.cpp
 */

#include <iostream>
 
using namespace std;
 
int main(int argc, char **argv)
{
    int n = 0;
    cout<<"Podaj liczbe: ";
    cin>>n;
   
    int i = 2;
    while(n%i > 0)
    {
        if(n==1)
        {
            cout<<"ani pierwsze ani zlozone"<<endl;
            break;
        }
        if(i*i > n)
        {
            cout<<"pierwsza"<<endl;
            break;
        }
        i++;
    }
    while(n%i == 0)
    {
        if(n==0)
        {
            cout<<"ani pierwsze ani zlozone"<<endl;
            break;
        }
        else if(n == 2)
        {
            cout<<"pierwsze";
            break;
        }
        cout<<"zlozona";
        break;
    }
    return 0;
}

