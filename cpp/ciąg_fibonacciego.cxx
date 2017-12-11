/*
 * ciąg_fibonacciego.cxx
 */


#include<iostream>
#include<cstdlib>
using namespace std;
 
int fib(int n)
{
	if(n<3)
		return 1;
		
	if(n>2)
		return fib(n-2)+fib(n-1);
		
}

 int fib_rek(int n)
{
    if (n < 2)
        return 1;
    else
        return fib_rek(n - 1) + fib_rek(n - 2);
    
}

int main()
{
 
  int n;
 
  cout<<"Podaj nr wyrazu ciągu: ";
  cin>>n;
 
  cout<<n<<" wyraz ciągu ma wartość "<<fib(n)<<endl;
 
  return 0;
}
