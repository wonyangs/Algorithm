N = int(input())

for i in range(1, N+1):
    print("*" * i + " " * (2*N-i * 2) + "*" * i)

for i in reversed(range(1, N)):
    print("*" * i + " " * (2*N-i * 2) + "*" * i)
