n,m=map(int,input().split())
p=[]
for i in range(n):
    a=input().split()
    for j,v in enumerate(a):
        if v=='1': p.append((i,j))
(r1,c1),(r2,c2)=p
print(abs(r1-r2)+abs(c1-c2))
