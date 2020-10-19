import pandas as pd 
import matplotlib.pyplot as plt

m = 244944
a = 1597
b = 5
x0 = 17
x = (a*x0 + b) % m
arr = []
x_list = []
y_list = []
bin = [0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.95,1]


# Push first 17 numbers
u = x/m
arr.append(u)
for i in range(16):
    x_list.append(u)
    x = (x*a + b)%m
    u = x/m
    arr.append(u)
    y_list.append(u)

#1000 values

for i in range(17,1000):
    x_list.append(u)
    u = arr[i-17] - arr[i-5]
    if(u<0):
        u = u+1
    arr.append(u)
    y_list.append(u)

plt.scatter(x_list,y_list,s=0.5)
plt.xlabel('x - axis') 
plt.ylabel('y - axis')
plt.savefig('180123015_q1_1000.png')
df = pd.DataFrame({'i=1000': arr})
graph = df.plot.hist(bins = bin, rwidth = 0.8)
graph.figure.savefig('180123015_q1_bargraph_i=1000.png')
plt.clf()

#10000 values
for i in range(1000,10001):
    x_list.append(u)
    u = arr[i-17] - arr[i-5]
    if(u<0):
        u = u+1
    arr.append(u)
    y_list.append(u)

plt.scatter(x_list,y_list,s=0.25)
plt.xlabel('x - axis') 
plt.ylabel('y - axis')
plt.savefig('180123015_q1_10000.png')
df = pd.DataFrame({'i=10000': arr})
graph = df.plot.hist(bins = bin, rwidth = 0.8)
graph.figure.savefig('180123015_q1_bargraph_i=10000.png')
plt.clf()

#100000 values
for i in range(10001,100001):
    x_list.append(u)
    u = arr[i-17] - arr[i-5]
    if(u<0):
        u = u+1
    arr.append(u)
    y_list.append(u)

plt.scatter(x_list,y_list, s=0.05)
plt.xlabel('x - axis') 
plt.ylabel('y - axis')
plt.savefig('180123015_q1_100000.png')
df = pd.DataFrame({'i=100000': arr})
graph = df.plot.hist(bins = bin, rwidth = 0.8)
graph.figure.savefig('180123015_q1_bargraph_i=100000.png')