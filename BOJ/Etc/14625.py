h1,m1=map(int,input().split())
h2,m2=map(int,input().split())
n=input().strip()
h,hm=h1,m1
c=0
while True:
    if n in f"{h:02d}{hm:02d}":
        c+=1
    if h==h2 and hm==m2:
        break
    hm+=1
    if hm==60:
        hm=0
        h+=1
print(c)
