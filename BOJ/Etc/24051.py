import sys
input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))
c = 0

for i in range(1, n):
    loc = i - 1
    new = a[i]
    
    while loc >= 0 and new < a[loc]:
        c += 1
        a[loc + 1] = a[loc]
        if c == k:
            print(a[loc + 1])
            exit()
        loc -= 1
    
    if loc + 1 != i:
        c += 1
        a[loc + 1] = new
        if c == k:
            print(a[loc + 1])
            exit()

print(-1)
