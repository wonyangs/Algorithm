import math
a=[9.23076,1.84523,56.0211,4.99087,0.188807,15.9803,0.11193]
b=[26.7,75,1.5,42.5,210,3.8,254]
c=[1.835,1.348,1.05,1.81,1.41,1.04,1.88]
t=[1,0,0,1,0,0,1]
T=int(input())
for _ in range(T):
    p=list(map(int,input().split()))
    s=0
    for i,v in enumerate(p):
        if t[i]:
            s+=math.floor(a[i]*(b[i]-v)**c[i])
        else:
            s+=math.floor(a[i]*(v-b[i])**c[i])
    print(s)
