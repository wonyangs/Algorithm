import sys
input = sys.stdin.readline

from collections import Counter

def func(depth):
    if len(s) == depth:
        print(''.join(ans))
        return
    
    for c in counter:
        if counter[c]:
            counter[c] -= 1
            ans.append(c)
            
            func(depth + 1)
            
            ans.pop()
            counter[c] += 1

for _ in range(int(input())):
    s = sorted(input().strip())
    counter = Counter(s)
    ans = []
    func(0)
