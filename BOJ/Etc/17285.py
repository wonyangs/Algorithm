t = input().rstrip()
p = "CHICKENS"
k = ord(t[0]) ^ ord(p[0])
for i in range(1, len(p)):
    if (ord(t[i]) ^ k) != ord(p[i]):
        k = ord(t[i]) ^ ord(p[i])

s = "".join(chr(ord(c) ^ k) for c in t)
print(s)
