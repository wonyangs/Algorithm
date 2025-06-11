n = int(input())
a = list(map(int, input().split()))
x, y = map(int, input().split())
rel = n * x // 100
abs_cnt = sum(1 for v in a if v >= y)
print(rel, abs_cnt)
