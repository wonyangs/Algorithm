N = int(input())
arr = sorted(map(int, input().split()))

MIN = float('inf')

for _ in range(N - 2):
    pivot = arr.pop()
    lit, rit = iter(arr), reversed(arr)
    left, right = next(lit), next(rit)
    
    for _ in range(len(arr) - 1):
        res = pivot + left + right
        if abs(res) < MIN:
            MIN = abs(res)
            ans = (left, right, pivot)
        
        if res < 0:
            left = next(lit)
        else:
            right = next(rit)
    if MIN == 0:
        break

print(*ans)
