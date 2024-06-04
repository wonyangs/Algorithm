from collections import defaultdict

N = int(input())
S = input()
dic = defaultdict(int)
for c in S:
    if c.isalpha():
        dic[c] += 1
print(sorted(dic.values())[-1])
