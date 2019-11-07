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
      
e = np.roots([9,-18,5])
if(e[0]>1):
	e =e[0]
elif(e[0]>1):
	e = e[1]

S = np.array([5,0])

a = np.linalg.norm(S[0])/e


k = e**2 - 1
A = a**2
b = np.sqrt(A*k)
print("a^2 - b^2 =",a**2  -  b**2)
len = 100
x = np.linspace(-10,10,len)
y1 = np.sqrt(((x/a)**2 - 1)*b)
y2 = -y1

H = np.hstack((np.vstack((x,y1)),np.vstack((x,y2))))
plt.plot(H[0,:len],H[1,:len],color='g',label="Hyberbola")
plt.plot(H[0,len+1:],H[1,len+1:],color='g')

ax.plot()
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() 
plt.axis('equal')
plt.show()
