A,B=input().split()
n,m=len(A),len(B)
for i in range(n):
    if A[i] in B:
        x,y=i,B.index(A[i])
        break
r=[['.']*n for _ in range(m)]
r[y]=list(A)
for j in range(m): r[j][x]=B[j]
for row in r: print("".join(row))
