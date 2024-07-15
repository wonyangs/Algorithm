a = input()
b = input()

arr = []
for c in a:
    if c.isalpha():
        arr.append(c)

a = ''.join(arr)

print(1 if b in a else 0)
