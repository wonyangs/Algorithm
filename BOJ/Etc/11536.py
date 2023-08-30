arr = [input() for _ in range(int(input()))]
cnt = 0
for i in range(len(arr)-1):
    if arr[i] < arr[i+1]:
        cnt += 1
    elif arr[i] > arr[i+1]:
        cnt -= 1
if cnt == len(arr) - 1:
    print("INCREASING")
elif -1 * cnt == len(arr) - 1:
    print("DECREASING")
else:
    print("NEITHER")
