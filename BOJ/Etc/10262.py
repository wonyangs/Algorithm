from collections import Counter
a1,b1,a2,b2=map(int,input().split())
c1,d1,c2,d2=map(int,input().split())
cg=Counter()
for i in range(a1,b1+1):
    for j in range(a2,b2+1):
        cg[i+j]+=1
ce=Counter()
for i in range(c1,d1+1):
    for j in range(c2,d2+1):
        ce[i+j]+=1
gw=ew=0
for x,cx in cg.items():
    for y,cy in ce.items():
        if x>y: gw+=cx*cy
        elif y>x: ew+=cx*cy
if gw>ew: print("Gunnar")
elif ew>gw: print("Emma")
else: print("Tie")
