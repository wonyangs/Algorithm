import sys

input = sys.stdin.readline

n, q = map(int, input().split())
a = [0] * (n + 1)
s = [0] * (n + 1)

for _ in range(q):
    tmp = input().split()
    if tmp[0] == '1':
        p = int(tmp[1])
        x = int(tmp[2])
        a[p] += x
    else:
        p = int(tmp[1])
        r = int(tmp[2])
        for i in range(1, n + 1):
            s[i] = s[i - 1] + a[i]
        print(s[r] - s[p - 1])
