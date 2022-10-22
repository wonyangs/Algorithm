b=list(map(int,input().split()))
a=list(map(int,input().split()))
res = 0
for i in range(3):
    if b[i] - a[i] < 0:
        res+=a[i]-b[i]
print(res)
