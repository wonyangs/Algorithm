arr = [0, 1]

for i in range(2, 305):
    arr.append(arr[-1] + i)

for _ in range(int(input())):
    res = 0
    n = int(input())
    for i in range(1, n+1):
        res += i * arr[i + 1]
    print(res)
        

