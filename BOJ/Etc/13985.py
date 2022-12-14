s = input().strip()
a, b, c = s[0], s[4], s[8]
if int(a) + int(b) == int(c):
    print("YES")
else:
    print("NO")
