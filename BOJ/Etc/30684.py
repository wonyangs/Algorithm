n = int(input())
print(min(s for s in (input() for _ in range(n)) if len(s) == 3))
