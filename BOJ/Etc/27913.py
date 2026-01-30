import sys

data = sys.stdin.read().split()
n = int(data[0])
q = int(data[1])

base = [1, 0, 0, 1, 0, 0, 1, 0, 0, 0]
arr = [base[i % 10] for i in range(n)]
cnt = sum(arr)

res = []
for k in range(q):
    x = int(data[k + 2]) - 1
    if arr[x]:
        arr[x] = 0
        cnt -= 1
    else:
        arr[x] = 1
        cnt += 1
    res.append(str(cnt))
        
sys.stdout.write('\n'.join(res))
