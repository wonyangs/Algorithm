p, r = map(int, input().split())
x = p / r

if x < 0.2:
    print('weak')
elif 0.2 <= x < 0.4:
    print('normal')
elif 0.4 <= x < 0.6:
    print('strong')
else:
    print('very strong')
