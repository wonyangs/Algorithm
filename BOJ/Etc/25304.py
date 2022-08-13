total = int(input())
n = int(input())
res = 0
for _ in range(n):
    price, cnt = map(int, input().split())
    res += price * cnt
print('Yes' if res == total else 'No')
