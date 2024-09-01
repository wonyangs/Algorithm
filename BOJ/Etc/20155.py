from collections import Counter

N, M = map(int, input().split())
print(Counter(map(int, input().split())).most_common(1)[0][1])
