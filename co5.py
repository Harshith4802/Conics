import numpy as np
import matplotlib.pyplot as plt

def line_gen(A,B):
  len =10
  x_AB = np.zeros((2,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB
  
def line_dir_pt(m,A,k1,k2):
  len =10
  x_AB = np.zeros((2,len))
  lam_1 = np.linspace(k1,k2,len)
  for i in range(len):
    temp1 = A + lam_1[i]*m
    x_AB[:,i]= temp1.T
  return x_AB


fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal')

e = 3/5
d = 6
a = d/(2*e)
b = a*np.sqrt(1 - e**2)
area = 2*a*b
print("The area of Quadrilateral is",area)
print("a = ",a)
print("b = ",b)


len = 100
x_elips = np.zeros((2,len))
thetha = np.linspace(0,2*np.pi,len)
x_elips[0,:] = a*np.cos(thetha)
x_elips[1,:] = b*np.sin(thetha)

plt.plot(x_elips[0,:],x_elips[1,:],label= 'Elipse')

B1 = np.array([0,b])
B2 = np.array([0,-1*b])
A1 = np.array([a,0])
A2 = np.array([-1*a,0])

l1 = line_gen(A1,B1) 
l4 = line_gen(A1,B2) 
l3 = line_gen(A2,B2) 
l2 = line_gen(B1,A2) 
plt.plot(l1[0,:],l1[1,:],color='r',label="Quadrilateral")
plt.plot(l2[0,:],l2[1,:],color='r')
plt.plot(l3[0,:],l3[1,:],color='r')
plt.plot(l4[0,:],l4[1,:],color='r')


ax.plot()
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() 
plt.axis('equal')
plt.show()
