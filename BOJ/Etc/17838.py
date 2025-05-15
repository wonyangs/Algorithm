t = int(input())

for _ in range(t):
    s = input()
    if len(s) != 7:
        print(0)
        continue
    if len(set(s)) != 2:
        print(0)
        continue
    if s[0] == s[1] and s[2] == s[3] and s[0] != s[2] and s[4] == s[0] and s[5] == s[6] == s[2]:
        print(1)
    else:
        print(0)
