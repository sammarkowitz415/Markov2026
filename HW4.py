#!/usr/bin/env python
# coding: utf-8

# In[5]:


# Homework 4 Question 4


import random
import numpy as np
import matplotlib.pyplot as plt
P = [[0,   1/2, 1/2, 0,   0  ],
     [1/4, 0,   0,   1/2, 1/4],
     [3/4, 0,   0,   0,   1/4],
     [0,   0,   0,   1,   0  ],
     [0,   0,   0,   0,   1  ]]
 
for start in [0, 1, 2]:
    foldtimes = []
    aggtimes = []
 
    for run in range(10000):
        x = start
        T = 0
        while x < 3:    
            u = random.random()
            total = 0
            for y in range(5):
                total = total + P[x][y]
                if u < total:
                    break
            x=y
            T=T+1
            if x ==3:
                foldtimes.append(T)
            else:
                aggtimes.append(T)
    print("start", start)
    print("  h    =", len(foldtimes) / 10000)
    print("  g    =", (sum(foldtimes) + sum(aggtimes)) / 10000)
    print("  tauF =", sum(foldtimes) / len(foldtimes))
    print("  tauA =", sum(aggtimes) / len(aggtimes))
 
    if start == 1:
        fold_I = foldtimes
        agg_I = aggtimes

Q = np.array([[0, 1/2, 1/2], [1/4, 0, 0], [3/4, 0, 0]])
R = np.array([[0, 0], [1/2, 1/4], [0, 1/4]])
 
ns = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
sim_fold, exact_fold, sim_agg, exact_agg = [], [], [], []
for n in ns:
    QR = np.linalg.matrix_power(Q, n - 1) @ R
    exact_fold.append(QR[1, 0] / (5/8))
    exact_agg.append(QR[1, 1] / (3/8))
    sim_fold.append(fold_I.count(n) / len(fold_I))
    sim_agg.append(agg_I.count(n) / len(agg_I))

plt.bar(ns ,sim_fold, label = 'Simulatiom')
plt.plot(ns, exact_fold, "ko", label="exact")
plt.title("Folded")
plt.xlabel("n")
plt.legend()
plt.show()

plt.bar(ns, sim_agg, label="simulation")
plt.plot(ns, exact_agg, "ko", label="exact")
plt.title("Aggregated")
plt.xlabel("n")
plt.legend()


# In[ ]:




