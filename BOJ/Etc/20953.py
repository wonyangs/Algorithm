import sys

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    n = a + b
    print(n * n * (n - 1) // 2)
