m, n, k = map(int, input().split())
a = [input() for _ in range(m)]

for row in a:
    b = ''
    for c in row:
        b += c * k
    for _ in range(k):
        print(b)
