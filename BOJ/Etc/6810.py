arr = [int(input()) for _ in range(3)]
res = 9 * 1 + 7 * 3 + 8 * 1 + 0 * 3 + 9 * 1 + 2 * 3 + 1 * 1 + 4 * 3 + 1 * 1 + 8 * 3
res += arr[0] + arr[2] + arr[1] * 3
print("The 1-3-sum is %d"%res)
