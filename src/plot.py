import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

folder_path = '/home/ccl2002/training/plt/'

mybb0 = np.loadtxt('output0.dat', delimiter = ' ')
t0 = mybb0[:, 0]
x0 = mybb0[:, 1]
t_ex0 = np.linspace(0,9,len(x0))
x_ex0 = np.exp(-3*t_ex0)
error=round(np.sum((x0-x_ex0)**2),3)
plt.plot(t_ex0,x_ex0, 'g-')
plt.plot(t0,x0, 'o')
plt.xlabel("step size: 10^(-6)")
plt.title("Graph 1, Error: "+str(error))
plt.legend(['analytical', 'numerical'])
plt.savefig(folder_path + "graph1.png")

mybb1 = np.loadtxt('output1.dat', delimiter = ' ')
t1 = mybb1[:, 0]
x1 = mybb1[:, 1]
t_ex1 = np.linspace(0,9,len(x1))
x_ex1 = np.exp(-3*t_ex1)
error=round(np.sum((x1-x_ex1)**2),3)
plt.plot(t_ex1,x_ex1, 'g-')
plt.plot(t1,x1, 'o')
plt.xlabel("step size: 10^(-5)")
plt.title("Graph 2, Error: "+str(error))
plt.legend(['analytical', 'numerical'])
plt.savefig(folder_path + "graph2.png")

mybb2 = np.loadtxt('output2.dat', delimiter = ' ')
t2 = mybb2[:, 0]
x2 = mybb2[:, 1]
t_ex2 = np.linspace(0,9,len(x2))
x_ex2 = np.exp(-3*t_ex2)
error=round(np.sum((x2-x_ex2)**2),3)
plt.plot(t_ex2,x_ex2, 'g-')
plt.plot(t2,x2, 'o')
plt.xlabel("step size: 10^(-4)")
plt.title("Graph 3, Error: "+str(error))
plt.legend(['analytical', 'numerical'])
plt.savefig(folder_path + "graph3.png")

mybb3 = np.loadtxt('output3.dat', delimiter = ' ')
t3 = mybb3[:, 0]
x3 = mybb3[:, 1]
t_ex3 = np.linspace(0,9,len(x3))
x_ex3 = np.exp(-3*t_ex3)
error=round(np.sum((x3-x_ex3)**2),3)
plt.plot(t_ex3,x_ex3, 'g-')
plt.plot(t3,x3, 'o')
plt.xlabel("step size: 10^(-3)")
plt.title("Graph 4, Error: "+str(error))
plt.legend(['analytical', 'numerical'])
plt.savefig(folder_path + "graph4.png")

mybb4 = np.loadtxt('output4.dat', delimiter = ' ')
t4 = mybb4[:, 0]
x4 = mybb4[:, 1]
t_ex4 = np.linspace(0,9,len(x4))
x_ex4 = np.exp(-3*t_ex4)
error=round(np.sum((x4-x_ex4)**2),3)
plt.plot(t_ex4,x_ex4, 'g-')
plt.plot(t4,x4, 'o')
plt.xlabel("step size: 10^(-2)")
plt.title(folder_path + "Graph 5, Error: "+str(error))
plt.legend(['analytical', 'numerical'])
plt.savefig(folder_path + "graph5.png")

mybb5 = np.loadtxt('output5.dat', delimiter = ' ')
t5 = mybb5[:, 0]
x5 = mybb5[:, 1]
t_ex5 = np.linspace(0,9,len(x5))
x_ex5 = np.exp(-3*t_ex5)
error=round(np.sum((x5-x_ex5)**2),3)
plt.plot(t_ex5,x_ex5, 'g-')
plt.plot(t5,x5, 'o')
plt.xlabel("step size: 10^(-1)")
plt.title("Graph 6, Error: "+str(error))
plt.legend(['analytical', 'numerical'])
plt.savefig(folder_path + "graph6.png")

mybb6 = np.loadtxt('output6.dat', delimiter = ' ')
t6 = mybb6[:, 0]
x6 = mybb6[:, 1]
t_ex6 = np.linspace(0,9,len(x6))
x_ex6 = np.exp(-3*t_ex6)
error=round(np.sum((x6-x_ex6)**2),3)
plt.plot(t_ex6,x_ex6, 'g-')
plt.plot(t6,x6, 'o')
plt.xlabel("step size: 1")
plt.title("Graph 7, Error: "+str(error))
plt.legend(['analytical', 'numerical'])
plt.savefig(folder_path + "graph7.png")
plt.close('all')
print("done")
