N = int(input())
a, b, c = map(int, input().split())
print(min(a, N) + min(b, N) + min(c, N))
