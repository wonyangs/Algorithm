N = int(input())
arr = [*map(int, input().split())]
c = int(input())

cnt = 0
for n in arr:
    cnt += (n // c)
    if n % c != 0:
        cnt += 1
print(cnt * c)
