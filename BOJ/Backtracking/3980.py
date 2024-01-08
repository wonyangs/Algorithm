import sys
input = sys.stdin.readline

def func(arr, i, hap, visited):
    global res
    
    if i == 11:
        res = max(res, hap)
        return
    
    for j in range(11):
        if arr[i][j] != 0 and visited & (1 << j) == 0:
            func(arr, i + 1, hap + arr[i][j], visited | (1 << j))
    
    
for _ in range(int(input())):
    arr = [[*map(int, input().split())] for _ in range(11)]
    res = 0
    func(arr, 0, 0, 0)
    print(res)
