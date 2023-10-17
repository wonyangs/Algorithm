N = int(input())
nums = list(map(int, input().split()))

result = 0
for i in range(N):
    for j in range(N):
        result += abs(nums[i] - nums[j])

print(result)
