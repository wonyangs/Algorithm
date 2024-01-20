for _ in range(int(input())):
    d = int(input())
    i = 0
    while i + i ** 2 <= d:
        i += 1
    print(i - 1)
