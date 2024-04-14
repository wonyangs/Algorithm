N = int(input())
for _ in range(N):
    print("@" * 5 * N)
for _ in range(3 * N):
    print("@" * N, end='')
    print("   " * N, end='')
    print("@" * N)
for _ in range(N):
    print("@" * 5 * N)
