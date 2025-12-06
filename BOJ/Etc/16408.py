from collections import Counter
c = input().split()
print(max(Counter(x[0] for x in c).values()))
