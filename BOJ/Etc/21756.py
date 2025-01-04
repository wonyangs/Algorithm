N=int(input())
a=list(range(1,N+1))
while len(a)>1:a=a[1::2]
print(a[0])
