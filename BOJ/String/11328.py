# Solved on 2022. 3. 19.
# 11328 Strfry

from collections import Counter
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    a, b = input().split()
    setA, setB = set(a), set(b)
    if setA != setB:
        print("Impossible")
        continue

    cntA, cntB = Counter(a), Counter(b)
    pos = True
    for c in setA:
        if cntA[c] != cntB[c]:
            print("Impossible")
            pos = False
            break
    
    if pos: print("Possible")
