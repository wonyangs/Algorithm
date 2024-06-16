import sys

input = sys.stdin.readline

arr = [0] + [i for i in range(1, 21)]
for _ in range(10):
    a, b = map(int, input().split())
    arr[a:b+1] = reversed(arr[a:b+1])
print(*(arr[1:]))
