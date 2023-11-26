for _ in range(int(input())):
    N, K = map(int, input().split())
    arr = [*map(int, input().split())]
    
    res = 0
    for n in arr:
        res += n // K
    print(res)
