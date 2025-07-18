n, m = map(int, input().split())

s = n * m

if s % 2 == 0:
    print(s)
else:
    print(s - 1)
