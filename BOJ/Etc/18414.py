x, l, r = map(int, input().split())
MIN = 1e9
res = 0
for i in range(l, r+1):
	if MIN > abs(x-i):
		MIN = min(MIN, abs(x-i))
		res = i
print(res)
