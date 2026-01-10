import sys

s = sys.stdin.readline().strip()
h = [3, 2, 1, 2, 3, 3, 3, 3, 1, 1, 3, 1, 3, 3, 1, 2, 2, 2, 1, 2, 1, 1, 2, 2, 2, 1]
a = [h[ord(c) - 65] for c in s]

while len(a) > 1:
    n = []
    for i in range(0, len(a), 2):
        if i + 1 < len(a):
            n.append((a[i] + a[i + 1]) % 10)
        else:
            n.append(a[i])
    a = n

if a[0] % 2:
    print("I'm a winner!")
else:
    print("You're the winner?")
