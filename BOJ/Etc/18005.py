n = int(input())
if n % 2 == 0:
    print(2 if (n // 2) % 2 == 0 else 1)
else:
    print(0)
