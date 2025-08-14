n = int(input())
x = n
a = 1
i = 2
while i * i <= x:
    c = 0
    while x % i == 0:
        x //= i
        c += 1
    if c:
        a *= c + 1
    i += 1
if x > 1:
    a *= 2
print(a)
