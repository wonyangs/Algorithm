N = int(input())
for _ in range(N):
    print("@@@" * N + " " * N + "@" * N)
for _ in range(3 * N):
    print("@" * N + " " * N + "@" * N + " " * N + "@" * N)
for _ in range(N):
    print("@" * N + " " * N + "@@@" * N)
