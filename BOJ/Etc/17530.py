N = int(input())
arr = [int(input()) for _ in range(N)]
if arr[0] == max(arr):
    print('S')
else:
    print('N')
