for _ in range(int(input())):
    s, a, b = input().split()
    a, b = int(a), int(b)
    for i, c in enumerate(s):
        if a <= i < b:
            continue
        print(c, end='')
    print()
