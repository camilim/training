#include <iostream>
#include <vector> 
#include <fstream>
#include <cmath>
using namespace std; 

double x0 = 1;
double t_beg = 0;
double t_end = 9;

int main()
{
 double dt[7]; //any variables to use
 ifstream inFile;
 inFile.open("params.dat");
 if (inFile.is_open())
 {
 	while (inFile >> dt[0]) 
	{ cout << dt[0] << endl;
	}
	inFile.close();
 }
 return 0;
}
//put name of width file
 /*cout<<("params_w.dat");
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
}*/
