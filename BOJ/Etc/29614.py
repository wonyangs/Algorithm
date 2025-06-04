s = input().strip()
d = {'A+': 4.5, 'A': 4.0, 'B+': 3.5, 'B': 3.0, 'C+': 2.5, 'C': 2.0, 'D+': 1.5, 'D': 1.0, 'F': 0.0}
n = len(s)
i = 0
t = 0.0
c = 0
while i < n:
    if s[i] in 'ABCD' and i + 1 < n and s[i+1] == '+':
        t += d[s[i:i+2]]
        i += 2
    else:
        t += d[s[i]]
        i += 1
    c += 1
print(t / c)
