for _ in range(int(input())):
    for i, c in enumerate(input()):
        if i == 0:
            print(c.upper(), end='')
        else:
            print(c,end='')
    print()
