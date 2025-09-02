a,b,n=map(int,input().split())
r=10**9
for _ in range(n):
    c,m=map(int,input().split())
    s=list(map(int,input().split()))
    try:
        i=s.index(a);j=s.index(b)
        if i<j:r=min(r,c)
    except ValueError:...
print(r if r<10**9 else -1)
