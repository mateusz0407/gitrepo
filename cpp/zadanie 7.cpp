

#include <iostream>
using namespace std;
int main(int argc, char **argv)
{
    int m = 0;
    for(int i=0 ;i<3;i++)
{
    cout << "podaj numer miesiaca:";
    cin >>m;
    if(m>0&& m<13)break;
    else cout<<"bledne dane"<<endl;
}
    switch(m)
    {
        case 1:
            cout<<"styczeń";
        break;
        case 2:
            cout<<"luty";
        break;
        case 3:
            cout<<"marzec";
        break;
        }
    return 0;
}

