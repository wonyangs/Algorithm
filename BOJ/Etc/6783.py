import sys

n = int(sys.stdin.readline())
t = s = 0

for _ in range(n):
    l = sys.stdin.readline().lower()
    t += l.count('t')
    s += l.count('s')

print("English" if t > s else "French")
