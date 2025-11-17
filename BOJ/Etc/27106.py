p = int(input())
c = 100 - p
q = c // 25
c %= 25
d = c // 10
c %= 10
n = c // 5
c %= 5
print(q, d, n, c)
