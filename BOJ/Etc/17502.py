n = int(input())
s = list(input())

for i in range(n // 2):
    l = s[i]
    r = s[-i - 1]
    if l == '?' and r == '?':
        s[i] = s[-i - 1] = 'a'
    elif l == '?':
        s[i] = r
    elif r == '?':
        s[-i - 1] = l

if n % 2 == 1 and s[n // 2] == '?':
    s[n // 2] = 'a'

print(''.join(s))
