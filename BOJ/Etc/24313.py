a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

print(1 if a0 <= (c - a1) * n0 and c - a1 >= 0 else 0)
