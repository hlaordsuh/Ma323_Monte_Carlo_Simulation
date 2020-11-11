import math
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
sigma=math.sqrt(variance)

#Take 30th September to be the starting date, S_0 corresponds to the stock price on Sep 30, 2020
# diff denotes the value of time interval between starting date and the required date
# diff ={4,9,14}
S_0=stock[-1]
val_1=0
val_2=0
val_3=0
for i in range(1000):
    Z=np.random.normal(mu,sigma,100)
    val_1+=S_0*math.exp(E*4 + sigma*(math.sqrt(4))*Z[3])
    val_2+=S_0*math.exp(E*9 + sigma*(math.sqrt(9))*Z[8])
    val_3+=S_0*math.exp(E*14 + sigma*(math.sqrt(14))*Z[13])

val_1/=1000
val_2/=1000
val_3/=1000
    
print("Mean:",mu)
print("Variance:",variance)

print("")

print("Estimated Value of stock price on 7 October 2020 is",val_1)
print("Actual Value of stock price on 7 October 2020 is",190.70	)
print("The Percentage error is :", (abs(190.70-val_1)/190.70)*100,"%")
print("Estimated Value of stock price on 14 October 2020 is",val_2)
print("Actual Value of stock price on 14 October 2020 is",200.05)
print("The Percentage error is :", (abs(200.05-val_2)/200.05)*100,"%")
print("Estimated Value of stock price on 21 October 2020 is",val_3)
print("Actual Value of stock price on 21 October 2020 is",203.75)
print("The Percentage error is :", (abs(203.75-val_3)/203.75)*100,"%")
    
            