import sys
input = sys.stdin.readline
n = int(input())
s = 0
for _ in range(n):
    s += sum(map(int, input().split()))
print(s)
