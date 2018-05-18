

#include <iostream>
using namespace std;
int main()
{
    float suma=0;
    int ilosc=0;
    int a=0;
    cout<<"wpisuj liczby tylko całkowite"<<endl;
    cout<<"podaj ilość liczb: "<<endl;
    cin>>ilosc;
    cout<<"podaj liczby: "<<endl;
    for (int i=0;i<ilosc;i++)
    {
        cin>>a;
        if(a<=0)
    {
        i=i-1;
        cout<<"podaj liczbe wiekszą od zera!"<<endl;
    }
        else
        suma=suma+a;
    }
    cout<<"suma tych cyfr wynosi: "<<suma<<"a ich srednia to:"<<suma/ilosc<<endl;
    return 0;
}


