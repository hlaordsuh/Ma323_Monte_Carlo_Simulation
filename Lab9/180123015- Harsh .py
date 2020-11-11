import numpy as np

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
sigma=np.sqrt(variance)

#Take 30th September to be the starting date, S_0 corresponds to the stock price on Sep 30, 2020
S_0=stock[-1]

K=1.1*S_0
#array to store the value/payoff of avg price Asian put option calculated without using control variate
Asian_put=[]
#array to store the value/payoff of European put option 
European_put=[]

for simulation in range(1000):
    #Generate N~ Poisson(lambda) for the counting process N(t)
    N=np.random.poisson(0.01,301)
    #Generate Normal distribution 
    Z=np.random.normal(0,1,301)
    #generate/simulate x and then exponentiate it to generate S
    X=[]
    X.append(np.log(S_0))
    for i in range(301):
        #if N=0 then M=0
        M=0
        #else M= sum(Y_j 1<=j<=N) where Y_j are distributed log-Normally
        if(N[i]!=0):
            LY=np.random.normal(mu,sigma,N[i])
            M=np.sum(LY)
        x=X[-1]+E*0.1+sigma*Z[i]*.316+M
        X.append(x)
    #Exponentiate X to get S
    S=np.exp(X)
    #append both the arrays with appropriate values/payoffs of both the put options according to their payoff formulae
    Asian_put.append(np.maximum(0,K-(np.sum(S)/301)))
    European_put.append(np.maximum(0,K-S[-2]))

#calculate the sample mean and sample variance of the Asian put option calculated without using control variate (mu_cap and var_cap as asked in the question)
mu_cap=np.mean(Asian_put)
var_cap=np.var(Asian_put)

#M=1000 sampling size
M=1000

#confidence interval
ci=[]
ci.append(mu_cap-((1.96*np.sqrt(var_cap))/np.sqrt(M)))
ci.append(mu_cap+((1.96*np.sqrt(var_cap))/np.sqrt(M)))

#sample mean and variance of European option 
sample_mean_Ep=np.mean(European_put)
sample_var_Ep=np.var(European_put)

# optimal b* can be estimated with bn_cap 
bn_cap=0
for i in range(1000):
    bn_cap+=(Asian_put[i]-mu_cap)*(European_put[i]-sample_mean_Ep)
bn_cap/=sample_var_Ep
bn_cap/=1000

#array to store the value/payoff of avg price Asian put option calculated using price of European option as control variate
Ap_with_control_variate=[]
for i in range(1000):
    price=Asian_put[i]-bn_cap*(European_put[i]-sample_mean_Ep)
    Ap_with_control_variate.append(price)

#sample mean and sample variance of the Asian put option calculated using price of European option as control variate
mu_with_control_variate=np.mean(Ap_with_control_variate)
var_with_control_variate=np.var(Ap_with_control_variate)

#confidence interval after using control variate
ci2=[]
ci2.append(mu_with_control_variate-((1.96*np.sqrt(var_with_control_variate))/np.sqrt(M)))
ci2.append(mu_with_control_variate+((1.96*np.sqrt(var_with_control_variate))/np.sqrt(M)))

print("Mean of the price of avg price Asian put option calculated without using control variate is:",mu_cap )
print("Variance of the price of avg price Asian put option calculated without using control variate is:", var_cap)
print("Confidence Interval without using the control variate: [",ci[0],",",ci[1],"]")
print("Mean of the same avg price Asian put option calculated by using the price of an European put as the control variate is:", mu_with_control_variate)
print("Variance of the same avg price Asian put option calculated by using the price of an European put as the control variate is:", var_with_control_variate)
print("Confidence Interval without using the control variate after using control variate: [",ci2[0],",",ci2[1],"]")