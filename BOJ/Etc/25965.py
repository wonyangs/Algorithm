for _ in range(int(input())):
    res = 0
    arr = [[*map(int, input().split())] for _ in range(int(input()))]
    k, d, a = map(int, input().split())
    for x, y, z in arr:
        res += max(k * x - d * y + a * z, 0)
    print(res)
