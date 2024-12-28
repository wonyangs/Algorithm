print("\n".join([str((lambda a, b: (a // b) ** 2)(*map(int, input().split()))) for _ in range(int(input()))]))
