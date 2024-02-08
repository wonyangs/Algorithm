a, b = map(int, input().split())

if min(a, b) + 1 > max(a, b):
    print(min(a, b) * 2)
else:
    print(min(a, b) * 2 + 1)
