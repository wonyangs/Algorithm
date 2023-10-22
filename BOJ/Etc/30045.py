res = 0
for _ in range(int(input())):
    s = input()
    if s.count('01') + s.count('OI'):
        res += 1
print(res)
