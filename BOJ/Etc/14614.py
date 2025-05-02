a, b, c = input().split()
a = int(a)
b = int(b)
if int(c[-1]) % 2 == 0:
    print(a)
else:
    print(a ^ b)
