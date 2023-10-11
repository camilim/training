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
    int i =0;
    while (inFile >> dt[i]) 
    { 
      i++;
    }
    inFile.close();
  }
  //int nt; put inside loop 
  
  for (int i=0; i < 7; i++)
  { 
    int nt = static_cast<int>((t_end-t_beg)/dt[i] + 1);
    vector<double> t(nt);
    vector<double> x(nt);
    t[0] = t_beg;
    x[0] = x0;                            
    for (int j=0; j < nt -1; j++)
    
    {
      x[j+1] = (1.0 - 3.0*dt[i])*x[j];
      t[j+1] = t[j] + dt[i];   
    }         		 
    ofstream myfile;
    myfile.open ("output.dat");
    for (int j=0; j < nt; j++)
    {

    myfile << t[j] << " " << x[j]  << endl;
    }
    myfile.close();
  } 
  return 0;
}
