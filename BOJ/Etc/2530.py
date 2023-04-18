a, b, c = map(int, input().split())
d = int(input())

t = a * 3600 + b * 60 + c + d

h = (t // 3600) % 24
m = (t % 3600) // 60
s = t % 60

print(h, m, s)
