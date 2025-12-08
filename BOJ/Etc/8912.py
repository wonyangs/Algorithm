import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    s = 0
    for i in range(1, n):
        for j in range(i):
            if a[j] <= a[i]:
                s += 1
    print(s)
