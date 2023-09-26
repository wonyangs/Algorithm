a, b = map(int, input().split())
if a - 1  > b:
    print(b + 1 + b)
else:
    print(a + a - 1)
