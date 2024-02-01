for n in range(1, int(input())+1):
    arr = [*map(int, input().split())]
    N, arr = arr[0], arr[1:]
    MAX = max(arr)
    MIN = min(arr)
    arr.sort()
    gap = 0
    for i in range(len(arr) - 1):
        gap = max(gap, arr[i+1] - arr[i])
    
    print("Class " + str(n))
    print(f"Max {MAX}, Min {MIN}, Largest gap {gap}")
