import sys
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]
arr.sort(reverse=True)
tip = 0

for i, n in enumerate(arr):
    if n - i > 0:
        tip += n - i
print(tip)
