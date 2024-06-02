N, M = map(int, input().split())
for i in range(N):
    for j in range(M):
        if (i + j) % 2 == 0:
            print("*", end='')
        else:
            print(".", end='')
    print()
