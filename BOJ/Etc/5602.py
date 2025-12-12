n,m=map(int,input().split())
c=[0]*m
for _ in range(n):
    a=list(map(int,input().split()))
    for j in range(m):
        c[j]+=a[j]
p=sorted(range(1,m+1),key=lambda x:(-c[x-1],x))
print(*p)
