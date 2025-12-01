import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))

s = 0
for i in range(n-1, -1, -1):
    s += a[i]
    if s >= m:
        print(i+1)
        exit()
print(-1)
