from math import lcm, gcd
for _ in range(int(input())):
    a, b = map(int, input().split())
    print(lcm(a, b), gcd(a, b))
