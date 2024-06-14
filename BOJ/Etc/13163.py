import sys
input = sys.stdin.readline

for _ in range(int(input())):
    arr = input().strip().split()
    arr[0] = "god"
    print(''.join(arr))
