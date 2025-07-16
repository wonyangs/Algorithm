n = int(input())
nums = []
ops = []
for i in range(2 * n - 1):
    if i % 2 == 0:
        nums.append(int(input()))
    else:
        ops.append(input().strip())
nums2 = [nums[0]]
ops2 = []
for o, v in zip(ops, nums[1:]):
    if o == '*':
        nums2[-1] = nums2[-1] * v
    elif o == '/':
        nums2[-1] = nums2[-1] // v
    else:
        ops2.append(o)
        nums2.append(v)
res = nums2[0]
for o, v in zip(ops2, nums2[1:]):
    if o == '+':
        res += v
    else:
        res -= v
print(res)
