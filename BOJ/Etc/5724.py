while True:
    N = int(input())
    if N == 0:
        break
    print(sum([i ** 2 for i in range(N+1)]))
