from collections import Counter

t = int(input())
for _ in range(t):
    b = Counter(input())
    w = int(input())
    for _ in range(w):
        wd = Counter(input())
        print("YES" if all(b[c] >= n for c, n in wd.items()) else "NO")
