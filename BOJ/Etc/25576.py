import sys
input = sys.stdin.readline

n, m = map(int, input().split())
l = list(map(int, input().split()))
c = 0
for _ in range(n - 1):
    k = list(map(int, input().split()))
    if sum(abs(k[i] - l[i]) for i in range(m)) > 2000:
        c += 1
print("YES" if c * 2 >= n - 1 else "NO")
