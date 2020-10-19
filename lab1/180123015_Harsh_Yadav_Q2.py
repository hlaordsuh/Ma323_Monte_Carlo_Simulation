import csv
import pandas as pd
import matplotlib.pyplot as plt

# q2_part(A)
# tabulated frequencies of numbers generated with 5 different values of x0 in q2.csv file
# a=1597
with open('q2.csv','w',newline='') as f2:
    writepointer=csv.writer(f2)
    arr_q2=['x0']
    r=0
    while r<100:
        arr_q2.append(str(r/100)+'-'+str((r+5)/100))
        r+=5
    writepointer.writerow(arr_q2)
    
    m=244944
    a=1597
    b=0
    arr_x0=[16,29,331,867,1000]
    for i in arr_x0:
        histo=[0,1]
        count=[0]*(len(arr_q2)-1)
        x=(a*i+b)%m
        u=x/m
        for j in range(10*m):
            k=(100*u)/5 
            count[int(k)]+=1
            histo.append(u)
            x=(a*x+b)%m
            u=x/m
        df = pd.DataFrame({
        'x0='+str(i): histo
        })
        hist = df.plot.hist(bins=20,rwidth=0.8)
        hist.figure.savefig('q2_plot_x0='+str(i)+'_a=1597.png')
        c=[i]
        c.extend(count)
        writepointer.writerow(c)

#q2_part(B)
#tabulated frequencies of numbers generated with 5 different values of x0 in q2b.csv file
#a=51749
with open('q2b.csv','w',newline='') as f3:
    writepointer=csv.writer(f3)
    arr_q2=['x0']
    r=0
    while r<100:
        arr_q2.append(str(r/100)+'-'+str((r+5)/100))
        r+=5
    writepointer.writerow(arr_q2)
    
    m=244944
    a=51749
    b=0
    arr_x0=[16,29,331,867,1000]
    for i in arr_x0:
        histo=[0,1]
        count=[0]*(len(arr_q2)-1)
        x=(a*i+b)%m
        u=x/m
        for j in range(10*m):
            k=(100*u)/5
            count[int(k)]+=1
            histo.append(u)
            x=(a*x+b)%m
            u=x/m
        df = pd.DataFrame({
        'x0='+str(i): histo
        })
        hist = df.plot.hist(bins=20,rwidth=0.8)
        hist.figure.savefig('q2_plot_x0='+str(i)+'_a=51749.png')
        c=[i]
        c.extend(count)
        writepointer.writerow(c)