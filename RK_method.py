# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 22:43:49 2019

@author: Trancrypt
"""

import numpy as np

a=0.0
b=2.0
N=10
alp=0.5

h=(b-a)/N
t=a
w=alp

def f(t,y):
    return y-(t**2)+1

for i in range(N+1):
    yt=((t+1)**2)-0.5*np.exp(t)
    print(w, " ", yt)
    K1 = h*f(t,w)
    K2 = h*f(t+h/2,w+K1/2)
    K3 = h*f(t+h/2,w+K2/2)
    K4 = h*f(t+h,w+K3)
    w = w+(K1+2*K2+2*K3+K4)/6
    t=a+(i+1)*h
