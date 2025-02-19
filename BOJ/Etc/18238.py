s = input().strip()
p = 'A'
t = 0
for c in s:
    d = abs(ord(c) - ord(p))
    t += min(d, 26-d)
    p = c
print(t)
