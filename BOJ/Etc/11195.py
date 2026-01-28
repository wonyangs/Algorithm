from collections import Counter

s = input()
c = Counter(s)
o = sum(v % 2 for v in c.values())

print(max(0, o - 1))
