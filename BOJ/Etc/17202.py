A, B = input(), input()
nums = [int(A[i//2] if i % 2 == 0 else B[i//2]) for i in range(16)]
while len(nums) > 2:
    nums = [(nums[i] + nums[i+1]) % 10 for i in range(len(nums)-1)]
print(f"{nums[0]}{nums[1]}")
