import sys
I=iter(sys.stdin.read().split())
for _ in range(int(next(I))):
    n=int(next(I));m=int(next(I))
    S=[0]*(n+1);A=[0]*(n+1)
    for _ in range(m):
        a=int(next(I));b=int(next(I));p=int(next(I));q=int(next(I))
        S[a]+=p;A[a]+=q;S[b]+=q;A[b]+=p
    V=[]
    for i in range(1,n+1):
        s=S[i]*S[i];t=A[i]*A[i]
        V.append(0 if s==t==0 else (1000*s)//(s+t))
    print(max(V));print(min(V))
