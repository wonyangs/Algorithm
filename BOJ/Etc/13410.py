N, M = map(int, input().split())
arr = [int(str(i * N)[::-1]) for i in range(1, M + 1)]
print(max(arr))
