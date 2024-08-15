n, nums = int(input()), list(map(int, input().split()))
line = []
for i, x in enumerate(nums): line.insert(i - x, i + 1)
print(*line)
