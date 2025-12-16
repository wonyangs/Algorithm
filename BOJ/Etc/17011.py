n = int(input())
for _ in range(n):
    s = input()
    r = []
    c = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            c += 1
        else:
            r.append(f"{c} {s[i-1]}")
            c = 1
    r.append(f"{c} {s[-1]}")
    print(' '.join(r))
