a,b,c=map(int,input().split())
d=[0]*(a+b+c+1)
for i in range(1,a+1):
    for j in range(1,b+1):
        for k in range(1,c+1):
            d[i+j+k]+=1
print(d.index(max(d)))