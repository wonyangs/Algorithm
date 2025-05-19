s = input()
p = "KOREA"
d = [-10**9] * 5
d[0] = 0
for c in s:
    for i in range(4, -1, -1):
        if c == p[i]:
            d[(i + 1) % 5] = max(d[(i + 1) % 5], d[i] + 1)
print(max(d))
