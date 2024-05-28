for _ in range(int(input())):
    N, M = map(int, input().split())
    if N < 12 or M < 4:
        print(-1)
        continue
    print(M * 11 + 4)
