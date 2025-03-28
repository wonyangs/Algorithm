a, b = map(int, input().split())
for n in range(1, min(a, b) + 1):
    if a % n == 0 and b % n == 0:
        print(n, a // n, b // n)
