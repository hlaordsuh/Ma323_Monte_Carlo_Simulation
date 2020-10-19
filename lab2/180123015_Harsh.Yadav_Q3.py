import math
import numpy as np
import matplotlib.pyplot as plt
import statistics

m = 244944
a = 1597
b = 5

arr = []

x0 = 19
x = x0

#1000 values
for i in range(1000):
    x = (a * x + b) % m
    u = x / m
    X = 0.5 - 0.5*np.cos(math.pi*u)
    arr.append(X)
print('Mean and variance for sample size = 1000')
print("Mean:"+str(statistics.mean(arr)) + " Variance:" + str(statistics.variance(arr)))


bins = []
k = 0.0
for i in range(101):
    bins.append(k)
    k = k + 1/100
values, base = np.histogram(arr, bins)
#evaluate the cumulative
cumulative = np.cumsum(values)
# plot the cumulative function
plt.plot(base[:-1], cumulative, c='blue', marker ='*', ms = 2)
plt.title('n=1000')
plt.text(.1, 100, 'Mean:'+str(statistics.mean(arr)) + " Variance:" + str(statistics.variance(arr)), style='italic')
plt.savefig('180123015_q3_1000.png')
plt.clf()

#100000 values
for i in range(1000,100000):
    x = (a * x + b) % m
    u = x / m
    X = 0.5 - 0.5*np.cos(math.pi*u)
    arr.append(X)
print('Mean and variance for sample size = 100000')
print("Mean:"+str(statistics.mean(arr)) + " Variance:" + str(statistics.variance(arr)))


values, base = np.histogram(arr, bins)
#evaluate the cumulative
cumulative = np.cumsum(values)
# plot the cumulative function
plt.plot(base[:-1], cumulative, c='blue', marker ='*', ms = 2)
plt.title('n=100000')
plt.text(.1, 10000, 'Mean:'+str(statistics.mean(arr)) + " Variance:" + str(statistics.variance(arr)), style='italic')
plt.savefig('180123015_q3_100000.png')
plt.clf()

#1000000 values
for i in range(100000,1000000):
    x = (a * x + b) % m
    u = x / m
    X = 0.5 - 0.5*np.cos(math.pi*u)
    arr.append(X)
print('Mean and variance for sample size = 1000000')
print("Mean:"+str(statistics.mean(arr)) + " Variance:" + str(statistics.variance(arr)))


values, base = np.histogram(arr, bins)
#evaluate the cumulative
cumulative = np.cumsum(values)
# plot the cumulative function
plt.plot(base[:-1], cumulative, c='blue', marker ='*', ms = 2)
plt.title('n=1000000')
plt.text(.1, 100000, 'Mean:'+str(statistics.mean(arr)) + " Variance:" + str(statistics.variance(arr)), style='italic')
plt.savefig('180123015_q3_1000000.png')
plt.clf()


#ACTUAL DISTRIBUTION FUNCTION
x = np.arange(0, 1, 0.01) 
# setting the corresponding y - coordinates 
#y = 0.5 - 0.5*np.cos(math.pi*x)
y = (2/math.pi)*np.arcsin(x**(0.5))
  
plt.plot(x, y,c='red') 
plt.savefig('180123015_q3_ActualFunction.png')