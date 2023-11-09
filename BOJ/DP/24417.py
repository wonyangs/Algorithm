def fibo(n):
    if n == 1 or n == 2:
        return 1
    a, b = 1, 1
    for _ in range(3, n+1):
        tmp = (a + b) % 1000000007
        a, b = b, tmp
    return b

N = int(input())
print(fibo(N), N-2)
