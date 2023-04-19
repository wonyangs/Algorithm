s, d = map(int, input().split())
a = (s + d) // 2
b = s - a

if (s + d) % 2 == 0 and a >= 0 and b >= 0:
    print(a, b)
else:
    print(-1)
