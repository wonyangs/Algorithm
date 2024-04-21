T = int(input())
N = int(input())
arr = [*map(int, input().split())]

if sum(arr) >= T:
    print("Padaeng_i Happy")
else:
    print("Padaeng_i Cry")
