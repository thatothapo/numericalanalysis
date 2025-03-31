# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 19:16:54 2020

@author: Trancrypt
"""

n=4
A=[[1,-1,2,-1,-8],[2,-2,3,-3,-20],[1,1,1,0,-2],[1,-1,4,3,4]]
m=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
x=[0]*n

for i in range(1,n):
   p=1
#   if A[p][i]==0:
#       break
   if p != i:
       temp=A[p]
       A[p], A[i]=A[i], temp
   for j in range(i+1,n):
       m[j][i]=A[j][i]/A[i][i]
       for q in range(5):
           A[j][q]=A[j][q]-m[j][i]*A[i][q]
       
#if A[n][n]==0:
    
x[n-1]=A[n-1][n]/A[n-1][n-1]

for i in range(n-1,1):
    sums=0
    for j in range(i+1,n):
        sums=sums+A[i][j]*x[j]
    x[i]=(A[i][n+1]-sums)/A[i][i]
    
print(x)