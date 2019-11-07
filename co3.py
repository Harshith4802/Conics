import numpy as np
import matplotlib.pyplot as plt

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

V = np.array(([25,0],[0,9]))
V1 = V/225
P = np.array([3,5*(3**0.5)])*0.5

len =1000
eigval,eigvec = np.linalg.eig(V1)
D = np.diag(eigval)
T = eigvec
y = np.zeros((2,len))
thetha = np.linspace(0,2*np.pi,len)
y[0,:] = ((1/D[0,0])**0.5)*np.cos(thetha)
y[1,:] = ((1/D[1,1])**0.5)*np.sin(thetha)


if(D[1,1] > D[0,0]):
   e = np.sqrt(1 - (D[0,0]/D[1,1]))
   F1 = np.array([((1/D[0,0])**0.5)*e,0])
   F2 = np.array([(-1*(1/D[0,0])**0.5)*e,0])
else:
   e = np.sqrt(1 - (D[1,1]/D[0,0]))
   F1 = np.array([0,((1/D[1,1])**0.5)*e])
   F2 = np.array([0,(-1*(1/D[1,1])**0.5)*e])
   
n = V@P
l1 = np.absolute((n@(F1 - P))/np.linalg.norm(n))
l2 = np.absolute((n@(F2 - P))/np.linalg.norm(n))

omat = np.array(([0,1],[-1,0]))
m = omat@n
T = line_dir_pt(m,P,-0.2,0.2)
plt.plot(T[0,:],T[1,:],label='Tangent at P')
m = omat@n
plt.plot(y[0,:],y[1,:],label='Elipse')
K1 = line_dir_pt(n,F1,-0.2,0.2)
plt.plot(K1[0,:],K1[1,:])
m = omat@n
K2 = line_dir_pt(n,F2,-0.2,0.2)
plt.plot(K2[0,:],K2[1,:])
print("d1 x d2 = ",l1*l2)

plt.plot(F1[0], F1[1], '.')
plt.text(F1[0] * (1 + 0.03), F1[1] * (1 - 0.1) , 'S1')

plt.plot(F2[0], F2[1], '.')
plt.text(F2[0] * (1 + 0.03), F2[1] * (1 - 0.1) , 'S2')

plt.plot(P[0], P[1], '.')
plt.text(P[0] * (1 + 0.03), P[1] * (1 - 0.1) , 'P')

ax.plot()
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc=1)
plt.grid() # minor
plt.axis('equal')
plt.show()
