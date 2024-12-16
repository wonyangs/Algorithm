import sys
from collections import defaultdict

input = sys.stdin.readline

for _ in range(int(input())):
    W = input().strip()
    K = int(input())
    dic = defaultdict(list)
    
    for i, c in enumerate(W):
        dic[c].append(i)
    
    dic = {k: v for k, v in dic.items() if len(v) >= K}
    if len(dic.keys()) == 0:
        print(-1)
        continue
    
    MIN, MAX = float('inf'), 0
    for lst in dic.values():
        for i in range(len(lst) - K + 1):
            diff = lst[i + K - 1] - lst[i] + 1
            MIN = min(MIN, diff)
            MAX = max(MAX, diff)
    print(MIN, MAX)
    
