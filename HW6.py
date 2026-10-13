#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Problem 1c

import numpy as np

for m in range(3, 13):
    P = np.zeros((m, m))
    for i in range(m - 1):
        P[i, i + 1] = 1     
    P[m - 1, 0] = 0.5         
    P[m - 1, 1] = 0.5          

    B = (P > 0)                
    M = 1
    while not B.all():         
        B = (B @ P > 0)        
        M = M + 1

    
    eigenvalues = np.linalg.eigvals(P)
    moduli = np.abs(eigenvalues)
    moduli = np.sort(moduli)  
    lambda2 = moduli[-2]       

  
    bound = (m - 1)**2 + 1
    print("m =", m, "  M =", M, "  (m-1)^2+1 =", bound, "  |lambda_2| =", round(lambda2, 4))


# In[4]:


# Problem 2

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

games = pd.read_csv('big12.csv')
teams = sorted(set(games['home']))
m = len(teams)

def h(s,t):
    x = (s+1)/(s+t+2)
    return 0.5 +0.5*np.sign(x-1/2)*np.sqrt(2*x-1)
    


# In[ ]:




