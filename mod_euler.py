# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 10:33:29 2019

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
    w=w+(h/2)*(f(t,w)+f(t+h,w+(h*f(t,w))))
    t=a+((i+1)*h)