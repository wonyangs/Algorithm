C, K = map(int, input().split())
d = 10 ** K
res = ((C + d // 2) // d) * d
print(res)
