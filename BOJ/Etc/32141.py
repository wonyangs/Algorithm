import sys
input=sys.stdin.readline
n,H=map(int,input().split())
d=list(map(int,input().split()))
s=0
for i,x in enumerate(d,1):
    s+=x
    if s>=H:
        print(i)
        break
else:
    print(-1)
