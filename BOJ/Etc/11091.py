a = set('abcdefghijklmnopqrstuvwxyz')
for _ in range(int(input())):
    s = set(c.lower() for c in input() if c.isalpha())
    m = a - s
    print("pangram" if not m else "missing " + ''.join(sorted(m)))
