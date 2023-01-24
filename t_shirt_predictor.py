
import pandas as pd
import numpy as np
import math
x=pd.read_csv("t_shirt.csv")
print(x)

h=(x["Height"])
w=(x["Weight"])
t2=x["Result"]
a=[]
h1=int(input("Enter Height "))
w1=int(input("Enter Weight"))
a.append(h1)
a.append(w1)
#a=[5,50]
t1=[]
R=[]
d={}
L=[]
for i in range(len(h)):
    dic={}
    x=(h[i]-a[0])**2
    y=(w[i]-a[1])**2
    r=math.sqrt(x+y)
    t1.append(r)
    
    size=t2[i]
    dic[size]=r
    L.append(dic)
rank=[]
print("Distance ",t1)
rank=[]
d=t1
print("Distance ",d)
for i in range(1,4):
    b=min(d)
    rank.append(b)
    d.remove(b)
    
print("rank***************************************** : ",rank)
print("R::::",rank)

R=[]
k=0
R=[]
k=0
for i in L:
    for j in i:
        print("J",j)
        r=j
        print(i[j])
        check=i[j]
                
        if k <4:
            if check in rank:
                
                k=k+1
           
                R.append(r)
                print("R",R)
print("**********R",R)


s=0
m=0
l=0
xl=0
xx=0
x=0
Size={}
for i in R:
    if i =="S":
        s=s+1
    elif i=="M":
        m=m+1
    elif i=="L":
        l=l+1
    elif i=="XL":
        xl=xl+1
    elif i=="XX":
        xx=xx+1
    elif i=="X":
        x=x+1
LL=[s,m,l,xl,xx,x]
R=LL.index(max(LL))
print()
print()


if R==0:
    print("User T-Shurt Size May Be :   S  ")
elif R==1:
    print("User T-Shurt Size May Be :   M")
elif R==2:
    print("User T-Shurt Size May Be :   L")
elif R==3:
    print("User T-Shurt Size May Be :   XL")
elif R==4:
    print("User T-Shurt Size May Be :   XX")
elif R==5:
    print("User T-Shurt Size May Be :   X")

