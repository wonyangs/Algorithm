s = list(map(int, input().split(':')))
e = list(map(int, input().split(':')))
s_s = s[0] * 3600 + s[1] * 60 + s[2]
e_s = e[0] * 3600 + e[1] * 60 + e[2]
d = (e_s - s_s) % (24 * 3600)
print(d)
