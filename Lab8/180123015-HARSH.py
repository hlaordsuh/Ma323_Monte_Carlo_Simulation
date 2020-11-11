import math
import numpy as np
import matplotlib.pyplot as plt  

#SBI STOCK CLOSING PRICES
stock=[184.800003,185.449997,184.699997,188.050003,188.600006,191.899994,199.100006,195.600006,192.699997,186.050003,183.800003,186.25,188.199997,190.75,194.399994,192,198.25,191.949997,187.149994,189.449997,191.199997,186.550003,191.449997,192.25,191.600006,191.449997,190.949997,190.649994,193.800003,195.050003,203.300003,201.899994,196.5,193.100006,195.100006,197.050003,194.75,198.399994,201.449997,207.949997,209.850006,215.649994,224.850006,212,218.100006,216.25,213.149994,206.600006,207.899994,204.050003,194.850006,198.149994,202.699997,198.5,200.149994,198.199997,195.449997,192.600006,185.800003,186.199997,183.800003,176.350006,182.199997,187.25,185.050003,185.399994]
n=len(stock)

u=[]
#GENERATING Ui's
#14 working days till 21st
for i in range(1,n):
    ui = np.log(stock[i]/stock[i-1])
    u.append(ui)

E=np.mean(u)

variance=0

for i in u:
    t=(i-E)*(i-E)
    variance+=t

variance/=(len(u)-1)
mu=E+variance/2
sigma=math.sqrt(variance)

#Take 30th September to be the starting date, S_0 corresponds to the stock price on Sep 30, 2020
S_0=stock[-1]
#given values of lambda
lamb_arr=[.01,.05,.1,.2]

for lamb in lamb_arr:
    #Generate N~ Poisson(lambda) for the counting process N(t)
    N=np.random.poisson(lamb,1000)
    #Generate Normal distribution 
    Z=np.random.normal(0,1,1000)
    #generate/simulate x and then exponentiate it to generate S
    X=[]
    X.append(math.log(S_0))
    for i in range(1000):
        #if N=0 then M=0
        M=0
        #else M= sum(Y_j 1<=j<=N) where Y_j are distributed log-Normally
        if(N[i]!=0):
            LY=np.random.normal(mu,sigma,N[i])
            M=np.sum(LY)
        x=X[-1]+E+sigma*Z[i]+M
        X.append(x)
    #Exponentiate X to get S
    S=np.exp(X)

    # data to be plotted 
    x = np.arange(1, 1002)  
    y = np.array(S) 
    
    # plotting 
    plt.title("Path of S(t) for lambda = " + str(lamb))  
    plt.xlabel("Time")  
    plt.ylabel("Stock price")  
    plt.plot(x, y, color ="red")
    plt.grid()  
    plt.show()
    
            
