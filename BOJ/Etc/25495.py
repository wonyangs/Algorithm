n = int(input())
a = list(map(int, input().split()))
s = 0
c = 0
l = 0
for x in a:
    d = 2 if c != x else l * 2
    if s + d >= 100:
        s = c = l = 0
        continue
    s += d
    c = x
    l = d
print(s)
