a, b = map(int, input().split())
r = a % b
print(a // b, end='' if not r else '.')

i = 0
while r and i<1000:
    r *= 10
    print(r // b, end='')
    r %= b
    i += 1
