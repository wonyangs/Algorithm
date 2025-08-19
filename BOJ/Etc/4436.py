import sys

for s in sys.stdin.read().strip().splitlines():
    if not s:
        continue
    n = int(s)
    seen = set()
    k = 0
    while len(seen) < 10:
        k += 1
        seen |= set(str(n * k))
    print(k)
