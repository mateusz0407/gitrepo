
#include <iostream>

using namespace std;

int sumuj(int a, int b)  
{
    return a+b;
}

int  odejmij(int a, int b)  
{
    return a-b;
}
int  mnoz(int a, int b)  
{

    cout<<"iloczyn:"<<a*b<<endl;
    
    return a*b;
}

int  dziel(int a, int b)  
{
    if(b==0)
        cout<<"nie dziel przez zero !!!"<<endl;
    return a/b;
}
int main(int argc, char **argv)
{
    int a,b;
    cout<<"podaj liczby :";
    cin>>a>>b;
    
    int suma =sumuj(a,b);
    int roznica= odejmij (a,b);
    
    cout <<"suma: "<<suma<<endl;
    cout <<"różnica: "<<roznica<<endl;
    cout <<"iloczyn: "<<mnoz(a,b)<<endl;
    cout <<"iloraz: "<<dziel(a,b)<<endl;

        return 0;
}

 
