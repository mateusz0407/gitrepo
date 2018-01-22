#include <iostream>
 
using namespace std;
 
int main(int argc, char **argv)
{
    int n = 0;
    cout<<"Podaj liczbe: ";
    cin>>n;
    int i = 2;
    while(n%i != 0)
    {
        if(i*i >= n)
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
