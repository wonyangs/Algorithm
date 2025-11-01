r,k,m=map(int,input().split())
h=m//k
for _ in range(h):
    r//=2
    if r==0:
        break
print(r)
