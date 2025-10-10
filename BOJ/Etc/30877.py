import sys
input = sys.stdin.readline
n = int(input())
r = []
for _ in range(n):
    s, t = input().split()
    for i in range(len(s)):
        if s[i] == 'x' or s[i] == 'X':
            r.append(t[i].upper())
            break
print(''.join(r))
