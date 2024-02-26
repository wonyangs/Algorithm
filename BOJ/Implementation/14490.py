n, m = map(int, input().split(':'))

for i in range(2, min(n, m) + 1):
    while n % i == 0 and m % i == 0:
        n //= i
        m //= i
print(f"{n}:{m}")
