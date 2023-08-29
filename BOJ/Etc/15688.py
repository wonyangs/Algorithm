import sys
input = sys.stdin.readline

arr = [int(input()) for _ in range(int(input()))]
arr.sort()
for n in arr:
    print(n)
