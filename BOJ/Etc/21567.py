a = int(input())
b = int(input())
c = int(input())
p = a * b * c
s = str(p)
for i in range(10):
    print(s.count(str(i)))
