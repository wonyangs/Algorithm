T = int(input())
for i in range(T):
    N = int(input())
    print("#" * N)
    for _ in range(N - 2):
        print("#" + 'J' * (N - 2) + "#")
    if N != 1:
        print("#" * N)
    print()
