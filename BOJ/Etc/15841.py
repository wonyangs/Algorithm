def f(n):
    if n <= 2:
        return 1
    a, b = 1, 1
    for i in range(3, n + 1):
        a, b = b, a + b
    return b

while True:
    h = int(input())
    if h == -1:
        break
    print(f"Hour {h}: {f(h)} cow(s) affected")
