R,C=map(int,input().split())
G=[input() for _ in range(R)]
cnt=[0]*5
for i in range(R-1):
    for j in range(C-1):
        s=G[i][j]+G[i][j+1]+G[i+1][j]+G[i+1][j+1]
        if '#' in s:continue
        cnt[s.count('X')]+=1
for x in cnt:print(x)
