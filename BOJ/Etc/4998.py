while True:
    try:
        n, b, m = map(float, input().split())
        y = 0
        while n < m:
            n += n * b / 100
            y += 1
        print(y)
    except EOFError:
        break
