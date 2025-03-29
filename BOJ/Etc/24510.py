c = int(input())
m = 0
for _ in range(c):
    s = input()
    x = s.count('for') + s.count('while')
    if x > m:
        m = x
print(m)
