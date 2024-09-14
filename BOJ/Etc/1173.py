N,m,M,T,R=map(int,input().split())
p=m; time=0; ex=0
if m+T>M:print(-1);exit()
while ex<N:
    time+=1
    if p+T<=M: p+=T; ex+=1
    else: p=max(m,p-R)
print(time)
