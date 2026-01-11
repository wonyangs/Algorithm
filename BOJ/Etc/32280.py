n = int(input())
s = []
t = ""
for _ in range(n + 1):
    a, b = input().split()
    if b == "teacher":
        t = a
    else:
        s.append(a)
l = input()
c = 0
for i in s:
    if i >= l and i >= t:
        c += 1
print(c)
