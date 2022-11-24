N = int(input())
print("Gnomes:")
for _ in range(N):
    arr = list(map(int, input().split()))
    if sorted(arr) == arr or sorted(arr)[::-1] == arr:
        print("Ordered")
    else:
        print("Unordered")
