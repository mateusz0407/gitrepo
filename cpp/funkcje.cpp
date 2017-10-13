
#include <iostream>

using namespace std;

void  sumuj(int a, int b)  
{

    cout<<"suma:"<<a+b<<endl;

}

void  odejmij(int a, int b)  
{

    cout<<"różnica:"<<a-b<<endl;

}
void  mnoz(int a, int b)  
{

    cout<<"iloczyn:"<<a*b<<endl;

}

void  dziel(int a, int b)  
{
    if (b=0)
    cout<<"nie dziel przez zero"<<endl;

    cout<<"iloraz:"<<a/b<<endl;

}
int main(int argc, char **argv)
{
    int a,b;
    cout<<"podaj liczby :";
    cin>>a>>b;
    
    
    sumuj(a,b);
    odejmij(a,b);
    mnoz(a,b);
    dziel(a,b);
        return 0;
}

