n = int(input())
a = [int(input()) for _ in range(n)]
avg = sum(a) // n
ans = sum(x - avg for x in a if x > avg)
print(ans)
