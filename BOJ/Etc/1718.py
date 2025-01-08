t, k = input(), input()

res = ''

for i in range(len(t)):
    if t[i] == ' ': 
        res += ' '
    else: 
        res += chr((ord(t[i]) - ord(k[i % len(k)]) - 1) % 26 + ord('a'))

print(res)
