a = input().strip()
b = input().strip()
h, m, s = map(int, a.split(':'))
c = h * 3600 + m * 60 + s
h, m, s = map(int, b.split(':'))
t = h * 3600 + m * 60 + s
if t <= c:
    t += 24 * 3600
d = t - c
hh = d // 3600
mm = (d % 3600) // 60
ss = d % 60
print(f"{hh:02d}:{mm:02d}:{ss:02d}")
