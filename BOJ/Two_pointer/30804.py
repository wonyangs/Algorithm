N = int(input())
arr = [*map(int, input().split())]

i, j, res = 0, 1, 0
nums = [0] * 10
nums[arr[i]] += 1
while j <= N:
    if sum(1 for n in nums if n > 0) <= 2:
        res = max(res, j - i)
        if j != N:
            nums[arr[j]] += 1
        j += 1
    else:
        nums[arr[i]] -= 1
        i += 1
print(res)
