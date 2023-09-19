#include <iostream>
#include <vector> 
#include <fstream> //allows me to create, read, and write to files
using namespace std;

int main()
{
 double x0=1, t, dt; //any variables to use
//the variables equal to the values that I set
 cout<<("params.dat");
 cin>>t;
//put name of width file
 cout<<("params_w.dat");
 cin>>dt;
 int nt = static_cast<int>((9)/dt + 1);
 std::vector<double> t(nt);
 std::vector<double> x(nt);

 t[0] = t[0]
 x[0] = x0;
 for (int i=0, i<nt -1, i++)
 { 
	x[i+1] = (1.0 - 3.0*dt)*x[i];
	t[i+1] = t[i] + dt;
 }
for (int i=0; i < nt; i++)
	{
	std::cout << "t[" << i << "] = " << t[i] << ", x[" <<i << "] = " << x[i] << std::endl;
	}
 return 0;
}
