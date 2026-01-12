c = 1
while True:
    try:
        line = input()
        if not line: break
        n = int(line)
        if n == 0: break
        h = list(map(int, input().split()))
        a = sum(h) // n
        k = sum(x - a for x in h if x > a)
        print(f"Set #{c}")
        print(f"The minimum number of moves is {k}.")
        print()
        c += 1
    except EOFError:
        break
