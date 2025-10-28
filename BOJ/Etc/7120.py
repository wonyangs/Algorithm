s = input()
r = ""
for i in range(len(s)):
    if i == 0 or s[i] != s[i-1]:
        r += s[i]
print(r)
