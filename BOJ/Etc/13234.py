s = input().strip().split()
a, op, b = s[0], s[1], s[2]
x = a == "true"
y = b == "true"
r = (x and y) if op == "AND" else (x or y)
print("true" if r else "false")
