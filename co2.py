import numpy as np
import matplotlib.pyplot as plt
import math

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

P  = np.array([2**0.5,3**0.5])
S1 = np.array([2,0])
S2 = np.array([-2,0])
O = np.array([0,0])
omat = np.array(([0,1],[-1,0]))

PS1 = np.linalg.norm(P - S1)
PS2 = np.linalg.norm(P - S2)

a = (np.absolute(PS1 -PS2))*0.5
e = np.linalg.norm(S1 -S2)/2*a

b = np.sqrt((a**2)*((e**2) - 1))

V = np.array(([a**-2,0],[0,-1*b**-2]))

eigval,eigvec = np.linalg.eig(V)
D = np.diag(eigval)
G = eigvec

len = 1000

y1 = np.linspace(-3,3,len)
y2 = np.sqrt((1 - V[0,0]*np.power(y1,2))/V[1,1])
y3 = -1*np.sqrt((1 - V[0,0]*np.power(y1,2))/V[1,1])
y = np.hstack((np.vstack((y1,y2)),np.vstack((y1,y3))))
plt.plot(y[0,:len],y[1,:len],color='g',label='Hyperbola')
plt.plot(y[0,len+1:],y[1,len+1:],color='g')
n = V@P
m = omat@n

P  = np.array([2**0.5,3**0.5])
T = line_dir_pt(m,P,-3,3)
plt.plot(T[0,:],T[1,:],label='Tangent at P')
plt.plot(P[0],P[1],'o')
plt.text(P[0] * (1 + 0.03), P[1] * (1 - 0.1) , 'P')
print(n,'x =',n@P)
ax.plot()
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc=1)
plt.grid() # minor
plt.axis('equal')
plt.show()
