for _ in range(int(input())):
    n, s = input().split()
    for i, c in enumerate(s):
        if i + 1 == n:
            continue
        print(c, end="")
    print()
