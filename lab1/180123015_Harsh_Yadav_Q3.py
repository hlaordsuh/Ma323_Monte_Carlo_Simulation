import csv
import pandas as pd
import matplotlib.pyplot as plt

# q3
# a = 1229; b = 1; m = 2048: Plot in a two-dimensional graph the points
# (ui-1, ui); i.e., the points (u1, u2), (u2, u3), (u3, u4),...
x0=16
a=1229
m=2048
b=1
x=(a*x0+b)%m
u=x/m
x_list=[]
y_list=[]
for i in range(1,10*m):
    x_list.append(u)
    x=(a*x+b)%m
    u=x/m
    y_list.append(u)

plt.scatter(x_list,y_list)
plt.xlabel('x - axis') 
plt.ylabel('y - axis')   
plt.savefig('q3_scattered_plot.png')
plt.show()
