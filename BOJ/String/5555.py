import sys
input = sys.stdin.readline

S = input().strip()
N = int(input())
cnt = 0
for _ in range(N):
    ring = input().strip() * 2
    if S in ring:
        cnt += 1
print(cnt)
