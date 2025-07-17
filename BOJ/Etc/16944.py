input()
s = input().strip()
t = '!@#$%^&*()-+'
m = sum([
    not any(c.isdigit() for c in s),
    not any(c.islower() for c in s),
    not any(c.isupper() for c in s),
    not any(c in t for c in s)
])
print(max(m, 6 - len(s)))
