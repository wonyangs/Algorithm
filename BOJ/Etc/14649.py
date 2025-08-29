p = int(input())
n = int(input())
r = [0] * 103
l = [0] * 103
for _ in range(n):
    x, d = input().split()
    (r if d == 'R' else l)[int(x)] += 1
pr = [0] * 103
for i in range(1, 101):
    pr[i] = pr[i - 1] + r[i]
sl = [0] * 104
for i in range(100, 0, -1):
    sl[i] = sl[i + 1] + l[i]
a = b = c = 0
for s in range(1, 101):
    m = (pr[s - 1] + sl[s + 1]) % 3
    a += m == 0
    b += m == 1
    c += m == 2
print(f"{p * a / 100:.2f}")
print(f"{p * b / 100:.2f}")
print(f"{p * c / 100:.2f}")
