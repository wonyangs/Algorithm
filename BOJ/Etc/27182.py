n, m = map(int, input().split())
if n - m == 14:
    print(n - 7)
else:
    if n <= 7:
        print(m + 7)
    else:
        print(n - 7)
