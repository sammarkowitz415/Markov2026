#!/usr/bin/env python
# coding: utf-8

# In[5]:


# Problem 3

#B Eigenvalues Numerically
import numpy as np


A = np.array([[-2, 2, 0,0], 
             [1,-3, 2, 0] ,
             [0, 2,-4, 2] ,
             [0, 0, 3, -3]])
print(np.linalg.eigvals(A))


# In[7]:


# Question 3 c


import numpy as np
from scipy.linalg import expm
import matplotlib.pyplot as plt
 
Q = np.array([[-2, 2, 0, 0],
              [1, -3, 2, 0],
              [0, 2, -4, 2],
              [0, 0, 3, -3]])
 
pi = np.array([3/19, 6/19, 6/19, 4/19])
 
x0 = np.array([1, 0, 0, 0])
 
eigs = np.linalg.eigvals(Q)
print(eigs)
lam2 = -1.511
 
t = np.linspace(0, 5, 501)
 
x0_list = []
x1_list = []
x2_list = []
x3_list = []
TV = []
 
for s in t:
    x = x0 @ expm(s * Q)
    x0_list.append(x[0])
    x1_list.append(x[1])
    x2_list.append(x[2])
    x3_list.append(x[3])
    TV.append(0.5 * np.sum(np.abs(x - pi)))
 
for i in range(len(t)):
    if TV[i] < 0.01:
        print("TV = 0.01 at t =", t[i])
        break
 
print("ln(100)/|lam2| =", np.log(100) / 1.511)
 
plt.plot(t, x0_list)
plt.plot(t, x1_list)
plt.plot(t, x2_list)
plt.plot(t, x3_list)
plt.legend(["x0", "x1", "x2", "x3"])
plt.xlabel("t")
plt.ylabel("x(t)")
plt.savefig("plot1.png")
plt.show()
 
plt.figure()
plt.plot(t, TV)
plt.plot(t, np.exp(lam2 * t))
plt.yscale("log")
plt.legend(["TV", "slope lam2"])
plt.xlabel("t")
plt.ylabel("TV")
plt.savefig("plot2.png")
plt.show()


# In[ ]:





# In[ ]:




