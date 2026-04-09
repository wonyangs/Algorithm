n = int(input())
r = 0
for _ in range(n - 1):
    _, _, c = map(int, input().split())
    r ^= c
print(r)
