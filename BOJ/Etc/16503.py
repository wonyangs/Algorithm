import sys

t = sys.stdin.read().strip().split()
a, op1, b, op2, c = int(t[0]), t[1], int(t[2]), t[3], int(t[4])

def calc(x, op, y):
    if op == '+':
        return x + y
    if op == '-':
        return x - y
    if op == '*':
        return x * y
    s = (x < 0) ^ (y < 0)
    q = abs(x) // abs(y)
    return -q if s else q

left = calc(calc(a, op1, b), op2, c)
right = calc(a, op1, calc(b, op2, c))

print(min(left, right))
print(max(left, right))
