a, b, c = map(int, input().split())
n = int(input())
print((n // 2) * (2 * c + b) + (a + b + c if n % 2 else 0))
