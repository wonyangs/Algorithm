n=int(input())
for i in range(n):
    s=''
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1 or i==j or j==n-1-i:
            s+='*'
        else:
            s+=' '
    print(s)
