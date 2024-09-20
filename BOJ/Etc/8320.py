n = int(input())
print(sum(n // i - i + 1 for i in range(1, int(n**0.5) + 1)))
