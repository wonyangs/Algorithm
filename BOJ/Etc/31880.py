input()
s=sum(map(int,input().split()))
p=1
for x in map(int,input().split()):
    p*=x or 1
print(s*p)
