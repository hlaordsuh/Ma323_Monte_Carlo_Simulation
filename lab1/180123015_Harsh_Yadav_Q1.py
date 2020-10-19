import csv
import pandas as pd
import matplotlib.pyplot as plt

#q1_part(A)
# sequence generator for a=6,b=0,m=11 and x0 ranging from 0 to 10
# the sequence is tabulated in q1.csv
with open('q1.csv','w',newline='') as f:
    writepointer=csv.writer(f)
    arr = [0,1,2,3,4,5,6,7,8,9,10]
    ar=['x0=']*11
    for i in range(0,11):
        ar[i]+=str(i)
    writepointer.writerow(ar)
    
    for i in range(0,100):
        writepointer.writerow(arr)
        for j in range(0,11):
            arr[j]=(6*arr[j])%11

#q1_part(B)
# sequence generator for a=3,b=0,m=11 and x0 ranging from 0 to 10
# the sequence is tabulated in q1b.csv
with open('q1b.csv','w',newline='') as f1:
    writepointer=csv.writer(f1)
    arr = [0,1,2,3,4,5,6,7,8,9,10]
    ar=['x0=']*11
    for i in range(0,11):
        ar[i]+=str(i)
    writepointer.writerow(ar)
    
    for i in range(0,100):
        writepointer.writerow(arr)
        for j in range(0,11):
            arr[j]=(3*arr[j])%11



