import numpy as np
import matplotlib.pyplot as plt

#mybb0 = np.loadtxt('output0.dat', delimiter = ' ')
#x0 = mybb0[:, 0]
#t0 = mybb0[:, 1]
#t_ex = np.linspace(0,9,len(x0))
#x_ex = np.exp(-3*t_ex)
#error=round(np.sum((x0-x_ex)**2),2)
#plt.figure()
#plt.plot(t_ex,x_ex, 'g-')
#plt.plot(x0,t0, 'o')
#plt.xlabel("step size: 10^(-6)")
#plt.title("Graph 1, Error: "+str(error))

#mybb1 = np.loadtxt('output1.dat', delimiter = ' ')
#x1 = mybb1[:, 0]
#t1 = mybb1[:, 1]
#t_ex = np.linspace(0,9,len(x1))
#x_ex = np.exp(-3*t_ex)
#error=round(np.sum((x1-x_ex)**2),2)
#plt.figure()
#plt.plot(t_ex,x_ex, 'g-')
#plt.plot(x1,t1, 'o')
#plt.xlabel("step size: 10^(-5)")
#plt.title("Graph 2, Error: "+str(error))

#mybb2 = np.loadtxt('output2.dat', delimiter = ' ')
#x2 = mybb2[:, 0]
#t2 = mybb2[:, 1]
#t_ex = np.linspace(0,9,len(x2))
#x_ex = np.exp(-3*t_ex)
#error=round(np.sum((x2-x_ex)**2),2)
#plt.figure()
#plt.plot(t_ex,x_ex, 'g-')
#plt.plot(x2,t2, 'o')
#plt.xlabel("step size: 10^(-4)")
#plt.title("Graph 3, Error: "+str(error))

#mybb3 = np.loadtxt('output3.dat', delimiter = ' ')
#x3 = mybb3[:, 0]
#t3 = mybb3[:, 1]
#t_ex = np.linspace(0,9,len(x3))
#x_ex = np.exp(-3*t_ex)
#error=round(np.sum((x3-x_ex)**2),2)
#plt.figure()
#plt.plot(t_ex,x_ex, 'g-')
#plt.plot(x3,t3, 'o')
#plt.xlabel("step size: 10^(-3)")
#plt.title("Graph 4, Error: "+str(error))

#mybb4 = np.loadtxt('output4.dat', delimiter = ' ')
#x4 = mybb4[:, 0]
#t4 = mybb4[:, 1]
#t_ex = np.linspace(0,9,len(x4))
#x_ex = np.exp(-3*t_ex)
#error=round(np.sum((x4-x_ex)**2),2)
#plt.figure()
#plt.plot(t_ex,x_ex, 'g-')
#plt.plot(x4,t4, 'o')
#plt.xlabel("step size: 10^(-2)")
#plt.title("Graph 5, Error: "+str(error))

#mybb5 = np.loadtxt('output5.dat', delimiter = ' ')
#x5 = mybb5[:, 0]
#t5 = mybb5[:, 1]
#t_ex = np.linspace(0,9,len(x5))
#x_ex = np.exp(-3*t_ex)
#error=round(np.sum((x5-x_ex)**2),2)
#plt.figure()
#plt.plot(t_ex,x_ex, 'g-')
#plt.plot(x5,t5, 'o')
#plt.xlabel("step size: 10^(-1)")
#plt.title("Graph 6, Error: "+str(error))

mybb6 = np.loadtxt('output6.dat', delimiter = ' ')
x6 = mybb6[:, 0]
t6 = mybb6[:, 1]
t_ex = np.linspace(0,9,len(x6))
x_ex = np.exp(-3*t_ex)
error=round(np.sum((x6-x_ex)**2),2)
plt.figure()
plt.plot(t_ex,x_ex, 'g-')
plt.plot(x6,t6, 'o')
plt.xlabel("step size: 1)")
plt.title("Graph 7, Error: "+str(error))

plt.legend(['analytical', 'numerical'])
plt.show()
