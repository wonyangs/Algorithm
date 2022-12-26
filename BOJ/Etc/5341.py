while True:
    N = int(input())
    if N == 0:
        break
    print(sum([i for i in range(1, N+1)]))
