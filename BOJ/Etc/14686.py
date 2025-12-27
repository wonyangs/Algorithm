n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

s1 = 0
s2 = 0
k = 0

for i in range(n):
    s1 += a[i]
    s2 += b[i]
    if s1 == s2:
        k = i + 1

print(k)
