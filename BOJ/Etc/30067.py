arr = [int(input()) for _ in range(10)]

hap = sum(arr)
for i in range(10):
    if arr[i] == hap - arr[i]:
        print(arr[i])
        break
