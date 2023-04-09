g, p, t = map(int, input().split())
if g + p * t > g * p:
    print(1)
elif g + p * t < g * p:
    print(2)
else:
    print(0)
