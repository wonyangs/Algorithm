import sys

data = sys.stdin.read().split()
i = 0
results = []
while i < len(data):
    if data[i] == "0":
        break
    n = int(data[i])
    p = int(data[i + 1])
    i += 2

    opp = n + 1 - p
    if p % 2:
        pages = {p, p + 1, opp, n - p}
    else:
        pages = {p, p - 1, opp, n + 2 - p}
    pages.discard(p)
    results.append(" ".join(map(str, sorted(pages))))

print("\n".join(results))
