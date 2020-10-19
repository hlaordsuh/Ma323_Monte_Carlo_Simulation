import matplotlib as plt
import math
import pandas as pd
import numpy as nm
from scipy.stats import beta

#Q1
#Two lists alpha1 and alpha2 contains 5 pairs of values with (a1,a2) pair as (alpha1[i],alpha2[i]) for i from 0 to 4 
alpha1=[2,1,3,4,7]
alpha2=[3,9,5,4,5]

#Q2
#x_star list containing x* values for each pair
x_star=[]
for i in range(5):
    x_star.append((alpha1[i]-1)/(alpha1[i]+alpha2[i]-2))

#Q3
#f list contains f(x*) values for respective x* values
f=[]
for i in range(5):
    c=beta.pdf(x_star[i],alpha1[i],alpha2[i])
    f.append(c)
    # print(c)
print(x_star)
print(f)
#Q4 and Q5 
#acceptance rejection method and histogram plots
bin = [0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.95,1]
for i in range(5):
    c=f[i]
    U1=[]
    a=nm.random.random_sample()
    f_a=beta.pdf(a,alpha1[i],alpha2[i])
    b=nm.random.random_sample()
    while(len(U1)<5000):
        if(c*b<=f_a):
            U1.append(a)
        b=nm.random.random_sample()
        a=nm.random.random_sample()
        f_a=beta.pdf(a,alpha1[i],alpha2[i])

    #plot histogram
    df = pd.DataFrame({'alpha1='+str(alpha1[i])+',alpha2='+str(alpha2[i])+' ': U1})
    graph = df.plot.hist(bins = bin, rwidth = 0.8,color='red')
    graph.figure.savefig('180123015'+'alpha1='+str(alpha1[i])+',alpha2='+str(alpha2[i])+' '+'.png')




