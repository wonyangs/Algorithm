import sys

while True:
    k = sys.stdin.readline().strip()
    if k == '0': break
    p = sys.stdin.readline().strip()
    n = len(k)
    r = []
    for i, c in enumerate(p):
        x = (ord(c) + ord(k[i % n]) - 129) % 26
        r.append(chr(x + 65))
    print(''.join(r))
