N = int(input())

for k in range(1, 10000):
    if 1 + k + k ** 2 == N:
        print(k)
        break
