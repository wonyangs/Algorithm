import sys
input = sys.stdin.readline
n, m = map(int, input().split())
b = list(map(int, input().split()))
for _ in range(m):
    a, l, r = map(int, input().split())
    if a == 1:
        b[l-1] = r
    elif a == 2:
        b[l-1:r] = [1 - x for x in b[l-1:r]]
    elif a == 3:
        b[l-1:r] = [0] * (r - l + 1)
    else:
        b[l-1:r] = [1] * (r - l + 1)
print(" ".join(map(str, b)))
