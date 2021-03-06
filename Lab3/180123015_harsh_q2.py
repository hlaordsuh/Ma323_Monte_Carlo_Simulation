# -*- coding: utf-8 -*-
"""180123015_harsh_q2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PcHsLg73RTSCUeyNb0h_-MOPNuxQD1YB
"""

hgg1=100000
import matplotlib.pyplot as plt
import math
import random 

c=[2.11,2.4,3.5]
def defcon2(x):
  kank=-4*x*x*x*x*x+15*x*x*x*x-20*x*x*x+10*x*x
  return kank
def defcon(root):
  root=root*(1-root)*(1-root)*(1-root)*20
  return root
def main_func(hj,hgg):
 print("  ")
 
 print("c used is")
 print(hj)
 print("Sample size is", hgg)
 
 main=[0]
 main.pop(0)
 cunt,k=0,0
 trial=[0]
 trial.pop(0)
 
 while cunt<hgg:
  k=k+1
  uu=random.random()
  u=random.random()  
  if uu<=defcon(u)/hj:
     main.append(u)
     cunt=cunt+1
     trial.append(k)
     k=0
 len2=len(main)
 len3=len(trial)
 sum=0
 for i in range(len3):
  sum=sum+trial[i]
 print("Average number of rejects")
 print(sum/len3)
 
 m1=[0]
 m1.pop(0)
 m2=[0]
 m2.pop(0)
 for i in range(10000):
   m2.append((i+1)/10000)
   m1.append(0)
 for i in range(len2):
   x=math.floor(main[i]*10000)
   m1[x]=m1[x]+1
 for i in range(10000):
   m1[i]=m1[i]/len2
 for i in range(9999):
   m1[i+1]=m1[i]+m1[i+1]
 max=0
 for i in range(10000):
   bv=abs(m1[i]-defcon2(m2[i]))
   if bv>max:
     max=bv
 print("Maximum difference in the original and sample distribution functions")
 print(max)
 plt.plot(m2,m1)
 

 plt.show()
 
 
for hj in c:
 main_func(hj,hgg1)
 main_func(hj,hgg1*15)

 plt.show()
 print("       JJJJJJJj ")
 print("           ")
 print("        *********      ************")