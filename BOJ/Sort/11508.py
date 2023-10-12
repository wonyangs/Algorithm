arr = [int(input()) for _ in range(int(input()))]
arr.sort(reverse=True)

res = 0
for i in range(2, len(arr), 3):
    res += arr[i-2] + arr[i-1]

res += sum(arr[len(arr)//3 * 3:])
print(res)
