n,m=map(int,input().split())
a,d=map(int,input().split())
sr,sc=map(int,input().split())
if sr==1:
    if d==0:f=sc<=a
    else:f=sc>=a
elif sr==n:
    if(n%2==1 and d==0)or(n%2==0 and d==1):f=0
    else:f=1
else:f=1
print("NO..."if f else"YES!")
