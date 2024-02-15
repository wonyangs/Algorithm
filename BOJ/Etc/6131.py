N = int(input())
arr = [i ** 2 for i in range(1, 501)]

cnt = 0
for i in range(0, 500):
    for j in range(i, 500):
        if arr[j] - arr[i] == N:
            cnt += 1
print(cnt)
