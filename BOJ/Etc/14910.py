n = list(map(int, input().split()))
print("Good" if all(x <= y for x, y in zip(n, n[1:])) else "Bad")
