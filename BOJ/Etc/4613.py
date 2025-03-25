while True:
    s = input()
    if s == '#':
        break
    ans = 0
    for i, c in enumerate(s, 1):
        if c != ' ':
            ans += i * (ord(c) - 64)
    print(ans)
