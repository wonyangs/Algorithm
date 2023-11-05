N, L = map(int, input().split())
arr = []
for _ in range(N):
    s = [i for i in input().split('0') if len(i) > 0]
    arr.append(len(s))
print(max(arr), arr.count(max(arr)))
