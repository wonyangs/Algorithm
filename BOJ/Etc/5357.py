for _ in range(int(input())):
    prev = ' '
    for c in input():
        if c != prev:
            print(c, end='')
            prev = c
    print()
