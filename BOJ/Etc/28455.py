n=int(input())
l=[int(input())for _ in range(n)]
l.sort(reverse=True)
t=l[:42]
s=sum(t)
c=0
for x in t:
    if x>=250:
        c+=5
    elif x>=200:
        c+=4
    elif x>=140:
        c+=3
    elif x>=100:
        c+=2
    elif x>=60:
        c+=1
print(s,c)
