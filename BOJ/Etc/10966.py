N = int(input())

for i in range(N * 2):
    if i % 2 == 0:
        print("* " * (N - (N // 2)))
    else:
        print(" *" * (N // 2))
