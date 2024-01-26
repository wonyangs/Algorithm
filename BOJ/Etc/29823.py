N = int(input())

a, b = 0, 0

for n in input():
    if n == 'N':
        a += 1
    elif n == 'S':
        a -= 1
    elif n == 'W':
        b += 1
    elif n == 'E':
        b -= 1
print(abs(a) + abs(b))
