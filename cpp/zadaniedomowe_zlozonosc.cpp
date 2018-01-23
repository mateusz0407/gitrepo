#include <iostream>
 
using namespace std;
 
int main(int argc, char **argv)
{
    int n = 0;
    cout<<"Podaj liczbe: ";
    cin>>n;
    int i = 2;
    while(i*i >= n)
    {
        if(n%i != 0)
        {
            cout<<"pierwsza"<<endl;
            break;
        }
        i++;
    }
    while(n%i == 0)
    {
        cout<<"zlozona";
        break;
    }
    return 0;
}
