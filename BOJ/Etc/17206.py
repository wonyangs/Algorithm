import sys

t, *arr = map(int, sys.stdin.read().split())
mx = max(arr)
s = [0] * (mx + 1)

for i in range(1, mx + 1):
    s[i] = s[i - 1]
    if i % 3 == 0 or i % 7 == 0:
        s[i] += i

for n in arr:
    print(s[n])
