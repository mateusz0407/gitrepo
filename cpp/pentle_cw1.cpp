
#include <iostream>
using namespace std;
int main(int argc, char **argv)
{
    // int i;
    int suma=0;
    int liczba=0;
    cout<<"wprowadzaj kolejne liczby:"<<endl;
    //for (;;)
    while(1)//pentla nieskonczona
    {
    cin>>liczba;
    cout<<"podano: "<<liczba<<endl;
    suma += liczba;
    if (suma > 75)
        break;
    };
    cout<<"suma liczby: "<<suma<<endl;
    return 0;
}
