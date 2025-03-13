s = list(input().strip())
t = int(input().strip())
for _ in range(t):
    a, b = map(int, input().split())
    s[a], s[b] = s[b], s[a]
print(''.join(s))
