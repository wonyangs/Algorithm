n = int(input())
a = list(map(int, input().split()))
c = sum(x % 2 for x in a)
print(1 if c == (n + 1) // 2 else 0)
