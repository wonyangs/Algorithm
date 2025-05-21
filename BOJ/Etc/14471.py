import sys
input=sys.stdin.readline
n,m=map(int,input().split())
cs=[];r=0
for _ in range(m):
    a,_=map(int,input().split())
    if a>=n:
        r+=1
    else:
        cs.append(n-a)
k=max(0,m-1-r)
cs.sort()
print(sum(cs[:k]))
