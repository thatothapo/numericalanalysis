# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 17:41:45 2020

@author: Trancrypt
"""

import numpy as np

##2nd or Taylor's method

#a=0.0
#b=2.0
#N=10
#alp=0.5
#
#h=(b-a)/N
#t=a
#w=alp
#
#def T2(t,y):
#    return (1+h/2)*(y-t**2+1)-h*t
#
#for i in range(N+1):
#    yt=((t+1)**2)-0.5*np.exp(t)
#    print(w, " ", yt)
#    w=w+h*T2(t,w)
#    t=h*(i+1)

##4th or Taylor's method
#
#a=0.0
#b=2.0
#N=10
#alp=0.5
#
#h=(b-a)/N
#t=a
#w=alp
#
#def T4(t,y):
#    return ((1+h/2+(h**2)/6+(h**3)/24)*(y-t**2))-((1+h/3+(h**2)/12)*(h*t))+1+h/2-(h**2)/6-(h**3)/24
#
#for i in range(N+1):
#    yt=((t+1)**2)-0.5*np.exp(t)
#    print(w, " ", yt)
#    w=w+h*T4(t,w)
#    t=h*(i+1)