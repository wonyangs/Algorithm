N, K = map(int, input().split())
res = True
for _ in range(int(input())):
    a = int(input())
    arr = list(map(int, input().split()))
    if K not in arr:
        res = False
print("YES" if res else "NO")
