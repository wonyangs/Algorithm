s = input()
p = "PER"
c = 0
for i in range(len(s)):
    if s[i] != p[i % 3]:
        c += 1
print(c)
