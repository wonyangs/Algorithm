n = int(input())
for _ in range(n):
    s = input()
    if s.startswith('Simon says'):
        print(s[10:])
