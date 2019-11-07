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


C1 = np.array([0,-6])
c = 1
r = np.sqrt(((np.linalg.norm(C1)**2) + c))
print(r)

len = 1000000
x_circ = np.zeros((2,len))
thetha = np.linspace(0,2*np.pi,len)
x_circ[0,:] = r *np.cos(thetha)
x_circ[1,:] = r *np.sin(thetha)
x_circ = (x_circ.T + C1).T

len= 99
V = np.array(([0,0],[0,1]))
y = np.linspace(-10,10,len)
x = np.power(y,2)/8
P = np.vstack((x,y))
m = np.array([1,1])
c1 = 6

G = np.array([2,-4])
T = line_gen(C1,G)

plt.plot(P[0,:],P[1,:],label="P") 
plt.plot(T[0,:],T[1,:]) 
P = P.T
plt.plot(G[0],G[1],'.')
plt.text(G[0] * (1 + 0.03), G[1] * (1 - 0.1) , 'P')
plt.plot(C1[0],C1[1],'.')
plt.text(C1[0] * (1 + 0.03), C1[1] * (1 - 0.1) , 'C1')
plt.plot(x_circ[0,:],x_circ[1,:],label="C")

omat = np.array(([0,1],[-1,0]))
		
ax.plot()
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() 
plt.axis('equal')
plt.show()
