from collections import Counter

s = input()
v = sorted(Counter(s).values(), reverse=True)
print(sum(v[2:]))
