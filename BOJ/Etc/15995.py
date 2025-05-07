a, m = map(int, input().split())

def egcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x, y = egcd(b, a % b)
    return g, y, x - (a // b) * y

_, x, _ = egcd(a, m)
x %= m
print(x)
