import sys

s = sys.stdin.read().strip()
k = 1

for i in range(1, len(s)):
    if s[i] <= s[i-1]:
        k += 1

print(k)
