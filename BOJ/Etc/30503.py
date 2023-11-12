N = int(input())
arr = [0] + [*map(int, input().split())]

for _ in range(int(input())):
    cmd = input().split()
    if cmd[0] == '1':
        l, r, k = map(int, cmd[1:])
        print(arr[l:r+1].count(k))
    else:
        l, r = map(int, cmd[1:])
        for i in range(l, r+1):
            arr[i] = 0
