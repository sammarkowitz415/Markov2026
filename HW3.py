#!/usr/bin/env python
# coding: utf-8

# In[2]:


import math
import time
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.special import erf


# In[6]:


p = np.array([[0.9, 0.1, 0.0],
              [0.0, 0.75, 0.25],
              [0.5, 0.0, 0.5]])

P = np.eye(3)          # p^0 = identity
for k in range(50):
    P = P @ p          # one more factor of p

print(np.round(P, 6))


# In[ ]:


p = np.array([[0.5, 0.5, 0,0 , 0, 0],
              [0.3, 0, 0.3, 0, 0.33, 0],
              [0, 0, 0.25, ]])

P = np.eye(3)          # p^0 = identity
for k in range(50):
    P = P @ p          # one more factor of p

print(np.round(P, 6))


# In[7]:


p = np.array([
    [1/2, 1/2,   0,   0,   0, 0],
    [1/3,   0, 1/3,   0, 1/3, 0],
    [  0,   0, 1/4, 3/4,   0, 0],
    [  0,   0,   1,   0,   0, 0],
    [  0,   0,   0,   0,   0, 1],
    [  0,   0,   0,   0,   1, 0],
])


def power(p, n):
    """p^n by multiplying n times, the literal definition."""
    P = np.eye(6)
    for _ in range(n):
        P = P @ p
    return P


P20 = power(p, 20)
P21 = power(p, 21)

np.set_printoptions(precision=4, suppress=True, linewidth=140)
print("p^20 =\n", P20)
print("p^21 =\n", P21)


# In[3]:


R = 20000
T = 10000
d0 = 10
rng = np.random.default_rng(2026)



def survival(nlions):
    gap = np.full((R, nlions),d0)
    alive = np.ones(R, dtype=bool)
    S = np.empty(T+1)
    S[0] = 1
    for t in range (1,T+1):
        lambs = rng.integers(0,2, size=(R,1)) * 2 - 1
        lions = rng.integers(0, 2, size=(R, nlions)) * 2 - 1
        gap += lions - lambs           
        alive &= (gap != 0).all(axis=1)        
        S[t] = alive.mean()
    return S
S1 = survival(1)
S2 = survival(2)
t = np.arange(T+1)
def beta(S):
    ok = (t >= 100) & (S > 0)
    return -np.polyfit(np.log(t[ok]), np.log(S[ok]), 1)[0]

b1, b2 = beta(S1), beta(S2)
for tt in (100, 1000, 10000):
    print(f"t={tt:6d}  S2={S2[tt]:.4f}  S1^2={S1[tt]**2:.4f}")

tp = t[1:]
plt.loglog(tp, S1[1:], label="$S_1(t)$, one lion")
plt.loglog(tp, erf(d0 / (2 * np.sqrt(tp))), "k--", label=r"erf$(d_0/2\sqrt{t})$")
plt.loglog(tp, S2[1:], label="$S_2(t)$, two lions")
plt.loglog(tp, S1[1:]**2, ":", color="gray", label="$S_1(t)^2$")
plt.xlabel("t")
plt.ylabel("survival probability")
plt.title(rf"$\beta_1$ = {b1:.3f}, $\beta_2$ = {b2:.3f}   (fit over $10^2 \leq t \leq 10^4$)")
plt.legend()
plt.savefig('HW3.png')
plt.show()


# In[ ]:




