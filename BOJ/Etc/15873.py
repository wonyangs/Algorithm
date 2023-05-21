s = input()

if len(s) == 2:
    print(int(s[0]) + int(s[1]))
elif len(s) == 3 and s[2] == '0':
    print(int(s[0]) + int(s[1:]))
else:
    print(sum(map(int, s.replace('0', '0 ').split())))
