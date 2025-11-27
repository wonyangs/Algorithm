import sys
input = sys.stdin.readline

n, m = map(int, input().split())
s = set()
for _ in range(m):
    i, j, k = map(int, input().split())
    s.add((i, j, k))

c = 0
for i, j, k in s:
    if all((i+di, j+dj, k+dk) in s for di, dj, dk in [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]):
        c += 1
print(c)
