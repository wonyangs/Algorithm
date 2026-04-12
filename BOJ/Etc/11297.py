import sys

while 1:
    v = sys.stdin.readline().split()
    if not v or v == ['0', '0', '0']:
        break
    s = sum(map(int, v)) % 25 + 1
    t = sys.stdin.readline().replace('\n', '')
    print("".join(chr((ord(c) - 97 - s) % 26 + 97) if 'a' <= c <= 'z' else c for c in t))
