while (n := input()) != '0':
    print((int(n) - 1) % 9 + 1 if n != '0' else 0)
