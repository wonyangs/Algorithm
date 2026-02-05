n, q = map(int, input().split())
a = [int(input()) for _ in range(n)]
for _ in range(q):
    s, e = map(int, input().split())
    print(sum(a[s-1:e]))
