w,n=input().split()
n=int(n)
a=[]
for _ in range(n):
    a.append(list(map(int,input().split())))

m={1:1,2:5,5:2,8:8}

if w in 'UD':
    a=a[::-1]
else:
    for i in range(n):
        a[i]=a[i][::-1]

for i in range(n):
    for j in range(n):
        a[i][j]=m.get(a[i][j],'?')

for r in a:
    print(' '.join(map(str,r)))
