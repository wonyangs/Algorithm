k, n = map(int, input().split())
s = input()
k %= 26
r = []
for c in s:
    o = ord(c)
    if 65 <= o <= 90:
        r.append(chr(65 + (o - 65 + k) % 26))
    elif 97 <= o <= 122:
        r.append(chr(97 + (o - 97 + k) % 26))
    else:
        r.append(c)
print(''.join(r))
