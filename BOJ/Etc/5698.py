while True:
    s = input()
    if s == '*':
        break
    w = s.lower().split()
    f = w[0][0]
    print('Y' if all(x[0] == f for x in w) else 'N')
