import sys

sys.setrecursionlimit(10000)

def search(arr):
    if len(arr) == 0:
        return
    
    n = arr[0]
    idx = 1
    for i in range(1, len(arr)):
        if arr[i] > n:
            idx = i
            break
    search(arr[1:idx])
    search(arr[idx:])
    print(n)

arr = []
while True:
    try:
        n = int(input())
        arr.append(n)
    except:
        break
search(arr)
