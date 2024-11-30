while (n := int(input())) != 0:
    while n >= 10:
        n = sum(map(int, str(n)))
    print(n)
