n=int(input())
a=[ [input() for _ in range(5)] for _ in range(n)]
min_d=36
i0=j0=0
for i in range(n):
    for j in range(i+1,n):
        d=0
        for r in range(5):
            for c in range(7):
                if a[i][r][c]!=a[j][r][c]:
                    d+=1
        if d<min_d:
            min_d=d
            i0,j0=i+1,j+1
print(i0,j0)
