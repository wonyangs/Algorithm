s = input().strip()
c = s
t = 0
while True:
    c = c[-1] + c[:-1]
    t += int(c)
    if c == s:
        break
print(t)
