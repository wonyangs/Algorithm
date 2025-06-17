s=input().strip()
p=s.index('*')
su=sum(int(c)*(1 if i%2==0 else 3) for i,c in enumerate(s[:12]) if c!='*')
m=int(s[12])
w=1 if p%2==0 else 3
t=(-su-m)%10
for x in range(10):
    if w*x%10==t:
        print(x)
        break
