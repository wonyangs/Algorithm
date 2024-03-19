import sys
input = sys.stdin.readline

fac = [0, 1, 2, 6, 24, 120]

while True:
    N = input().strip()
    if N == '0':
        break
    cnt = len(N)
    res = 0
    for i in N:
        res += int(i) * fac[cnt]
        cnt -= 1
    print(res)
