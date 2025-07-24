n=int(input())
bs=10**30
x=y=z=0
for a in range(1,int(n**(1/3))+2):
    if n%a:continue
    m=n//a
    for b in range(a,int(m**0.5)+1):
        if m%b:continue
        c=m//b
        s=2*(a*b+b*c+c*a)
        if s<bs:
            bs=s
            x,y,z=a,b,c
print(x,y,z)
