N,*O=open(0).read().split();P={};C=0
for i in range(0,int(N)*2,2):c,p=O[i],O[i+1];C+=c in P and P[c]!=p;P[c]=p
print(C)
