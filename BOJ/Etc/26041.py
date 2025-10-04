a = input().split()
b = input()
c = 0
for p in a:
    if p != b and p.startswith(b):
        c += 1
print(c)
