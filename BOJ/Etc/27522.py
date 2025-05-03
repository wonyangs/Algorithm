s = []
for _ in range(8):
    t, team = input().split()
    m, s_, ms = map(int, t.split(':'))
    total_ms = m * 60 * 1000 + s_ * 1000 + ms
    s.append((total_ms, team))

s.sort()
score = [10, 8, 6, 5, 4, 3, 2, 1]
r, b = 0, 0
for i in range(8):
    if s[i][1] == 'R':
        r += score[i]
    else:
        b += score[i]

if r > b:
    print('Red')
elif b > r:
    print('Blue')
else:
    for i in range(8):
        if s[i][1] == 'R':
            print('Red')
            break
        elif s[i][1] == 'B':
            print('Blue')
            break
