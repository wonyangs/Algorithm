a,b,c=map(int,input().split())
i,j,k=map(int,input().split())
x=min(a/i,b/j,c/k)
print(a-i*x,b-j*x,c-k*x)
