import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [[*map(int, input().split())] for _ in range(N)]
A = int(input())
for _ in range(3):
    arr = list(zip(*arr[::-1]))

MAX = 0
for i in range(M-A+1):
    hap = 0
    for j in range(A):
        hap += sum(arr[i+j])
    MAX = max(MAX, hap)
print(MAX)
