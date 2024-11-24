N = int(input())
print(sum(1 for A in range(2, N, 2) for B in range(1, N - A) if N - A - B > B + 1))
