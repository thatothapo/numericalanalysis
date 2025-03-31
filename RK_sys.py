# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 22:43:49 2019

@author: Trancrypt
"""

import numpy as np

a=0.0
b=1.0
N=10
alp = [-0.4, -0.6]
m=2

h=(b-a)/N
t=a
w=[0,0]
K1=[0,0]
K2=[0,0]
K3=[0,0]
K4=[0,0]

def f(t,u1,u2):
    return [u2, (np.exp(2*t)*np.sin(t))-(2*u1)+(2*u2)]

for j in range(m):
    w[j] = alp[j]
    
    
for i in range(N+1):
    print(w)
    for j in range(m):
        K1[j] = h*f(t,w[0],w[1])[j]
    for j in range(m):
        K2[j] = h*f(t+h/2,w[0]+K1[0]/2,w[1]+K1[1]/2)[j]
    for j in range(m):
        K3[j] = h*f(t+h/2,w[0]+K2[0]/2,w[1]+K2[1]/2)[j]
    for j in range(m):
        K4[j] = h*f(t+h,w[0]+K3[0],w[1]+K3[1])[j]
    for j in range(m):
        w[j] = w[j]+(K1[j]+2*K2[j]+2*K3[j]+K4[j])/6
    t=a+(i+1)*h



