a, b = map(int, input().split())

m = {0: 'R', 2: 'S', 5: 'P'}
x = m.get(a, 'V')
y = m.get(b, 'V')

if x == y:
    print('=')
elif x == 'V' and y != 'V':
    print('<')
elif y == 'V' and x != 'V':
    print('>')
elif (x, y) in {('R', 'S'), ('S', 'P'), ('P', 'R')}:
    print('>')
else:
    print('<')
