import sys

input = sys.stdin.read
data = input().split()

t = int(data[0])
arr = list(map(int, data[1:]))

pre = [0] * 1001

for n in range(1, 1001):
    s = 0
    for b in range(2, n + 1):
        x = n
        z = 0
        while x % b == 0:
            z += 1
            x //= b
        s += z
    pre[n] = s

out = [str(pre[n]) for n in arr]
print("\n".join(out))
