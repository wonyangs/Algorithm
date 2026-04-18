import sys
w = sys.stdin.read().split()
if w:
    k = int(w[0])
    i = 1
    for x in range(1, k + 1):
        b = int(w[i+1])
        n = int(w[i+2])
        r = int(w[i+3])
        i += 4
        s = set(w[i:i+b])
        i += b
        t = 0
        for _ in range(n):
            if w[i] in s:
                t += int(w[i+1]) * r // 100
            i += 2
        print(f"Data Set {x}:")
        print(t)
        print()
