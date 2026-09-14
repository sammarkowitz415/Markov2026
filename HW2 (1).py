#!/usr/bin/env python
# coding: utf-8

# In[3]:


import math
import time
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



# In[18]:


# Problem 3 c

N = 10000
lam = 0.5
c = 4/np.e
tries = 0
t0 = time.perf_counter()

samples = np.zeros(N)
i = 0

while i < N:
    u1 = random.random()
    y= -math.log(1 - u1)/lam
    fy = y*math.exp(-y)
    gy = lam*math.exp(-lam*y)
    u2= random.random()
    tries +=1
    if u2 < fy/(c*gy):
        samples[i] = y
        i += 1

x = np.linspace(0, 12, 400)
f = x*np.exp(-x)
time = time.perf_counter() - t0
print(N/tries, 1/c, time/N)


plt.hist(samples, bins = 60, density=True)
plt.plot(x,f, linewidth = 2, label=r'f(x)', color = 'black')
plt.title('Accept / Reject with Gamma Distribution')  

plt.show()

    


# In[8]:


# Problem 4


random.seed(0)


a =0.9 
lam_f = 1000
lam_s = 10
n = 100000
trials = np.zeros(n)
for i in range(n):
    u1 = random.random()
    if u1 < a:
        lam = lam_f
    else:
        lam = lam_s
    u2 = random.random()
    trials[i] = -np.log(u2)/lam



t = np.linspace(0.0001, 0.5, 2000)
plt.hist(trials, np.linspace(0, 0.5, 500), density=True)
plt.plot(t, a*lam_f*np.exp(-lam_f*t)+(1-a)*lam_s*np.exp(-lam_s*t))
plt.plot(t, a*lam_f*np.exp(-lam_f*t))
plt.plot(t, (1-a)*lam_s*np.exp(-lam_s*t))
plt.yscale('log')
plt.ylim(1e-2, 2e3)
plt.xscale('log')
plt.xlabel('dwell time')
plt.ylabel('density')
plt.show()




# In[13]:


# Question 5 b)

z = np.array([1-math.sqrt(1-random.random()) for x in range(100000)])
space = np.linspace(0,1,100)

plt.hist(z,bins=50, density=True)
plt.plot(space, 2*(1-space))
print(z.mean())
plt.show()



# In[15]:


# Problem 5 c

n = 10**4
r = 10**3
C = np.ones(r)
for N in range(3, n):
    p = C/ N
    C = C+ (np.random.random(r) <p)
z = C/ n

print(z.mean(), z.std()/z.mean())
space = np.linspace(0,1,100)

plt.hist(z, bins=50, density=True)
plt.plot(space, 2*(1-space))
plt.show()


# In[ ]:




