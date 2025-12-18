a, b, n, k = map(int, input().split())
s = (k - 1) // n
print(s // b + 1, s % b + 1)
