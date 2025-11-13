n = int(input())
d = len(str(n))
c = 0
while len(str(n * 2)) == d:
    n *= 2
    c += 1
print(c)
