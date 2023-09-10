N = int(input())
arr = [0] + [*map(int, input().split())]
for _ in range(int(input())):
    s, n = map(int, input().split())
    
    if s == 1:
        for i in range(n, N+1, n):
            arr[i] ^= 1
    else:
        i = 0
        while n + i <= N and n - i >= 1:
            if i == 0:
                arr[n] ^= 1
            else:
                if arr[n + i] == arr[n - i]:
                    arr[n + i] ^= 1
                    arr[n - i] ^= 1
                else:
                    break
            i += 1

for i in range(1, N+1):
    print(arr[i], end="")
    if i % 20 == 0:
        print()
    else:
        print(" ", end="")
