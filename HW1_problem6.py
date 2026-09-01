#!/usr/bin/env python
# coding: utf-8

# In[3]:


import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[10]:


X = np.random.uniform(0,1, 100000)
Y = np.random.uniform(0,1, 100000)
Z = np.random.uniform(0,1, 100000)
N = 100000
check = (X**2+Y**2<Z) & (Z**2>X*Y)
estimate = np.cumsum(check) / np.arange(1,N+1)
plt.plot( np.arange(1, N+1), estimate, label = 'Monte Carlo')
plt.axhline( 23*np.pi/192, label = 'Analytical Value')
plt.xscale('log')
plt.xlabel('Sample Size')
plt.ylabel('Estimated Probability')
plt.title('Monte Carlo Simulation for Problem 6')
print(estimate[-1])
plt.show()




# In[ ]:




