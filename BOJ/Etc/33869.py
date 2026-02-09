w = input()
s = input()
k = []

for c in w:
    if c not in k:
        k.append(c)

for i in range(26):
    c = chr(65 + i)
    if c not in k:
        k.append(c)

print(''.join(k[ord(c) - 65] for c in s))
