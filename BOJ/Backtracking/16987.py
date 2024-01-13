import sys
input = sys.stdin.readline

def func(arr, broke, i, N):
    global res

    res = max(res, bin(broke).count('1'))
    if i == N:
        return
    
    if (broke & (1 << i)) != 0:
        func(arr, broke, i + 1, N)
        return
    
    s, w = arr[i]
    for j in range(N):
        if i == j or (broke & (1 << j)) != 0:
            continue
        a, b = arr[j]
        new_arr = [t for t in arr]
        new_broke = broke
        if s - b <= 0:
            new_broke |= (1 << i)
        if a - w <= 0:
            new_broke |= (1 << j)
        new_arr[i] = (s - b, w)
        new_arr[j] = (a - w, b)
        
        func(new_arr, new_broke, i + 1, N)


N = int(input())
arr = [tuple([*map(int, input().split())]) for _ in range(N)]
res = 0
func(arr, 0, 0, N)
print(res)
