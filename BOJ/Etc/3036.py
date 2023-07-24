N = int(input())
arr = [*map(int, input().split())]
for i in range(1, N):
    a, b = arr[0], arr[i]
    for j in range(2, 1001):
        while a >= j and b >= j and a % j == 0 and b % j == 0:
            a //= j
            b //= j
    print(f"{a}/{b}")
