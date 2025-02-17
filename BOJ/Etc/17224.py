import sys
input = sys.stdin.readline

n, l, k = map(int, input().split())
s = []
for _ in range(n):
    a, b = map(int, input().split())
    if l < a:
        continue
    s.append(140 if l>=b else 100)
s.sort(reverse=True)
print(sum(s[:k]))
