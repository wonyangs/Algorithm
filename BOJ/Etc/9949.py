import sys
d = sys.stdin.read().splitlines()
i = 0
c = 1
while i < len(d):
    if d[i] == '# #':
        break
    if not d[i]:
        i += 1
        continue
    a, b = d[i].split()
    i += 1
    n = int(d[i])
    i += 1
    if c > 1:
        print()
    print(f"Case {c}")
    for _ in range(n):
        r = "".join(['_' if x.lower() in (a, b) else x for x in d[i]])
        print(r)
        i += 1
    c += 1
