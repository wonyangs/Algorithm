import sys
input = sys.stdin.readline

a, b = 0, 0
for _ in range(int(input())):
    x, y = map(int, input().split())
    if x > y:
        a += 1
    elif x < y:
        b += 1
print(a, b)
