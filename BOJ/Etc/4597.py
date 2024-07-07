import sys
input = sys.stdin.readline

while True:
    s = input().strip()
    if s == '#':
        break
    s, p = s[:-1], s[-1]
    cnt = s.count('1')
    if cnt % 2 == 0:
        if p == 'e':
            print(s + '0')
        else:
            print(s + '1')
    else:
        if p == 'e':
            print(s + '1')
        else:
            print(s + '0')
