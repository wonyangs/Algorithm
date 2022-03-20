# Solved on 2022. 3. 20.
# 2457 공주님의 정원

import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    arr.append(tuple(map(int, input().split())))
arr.sort()

res = []
tmp = None
for flower in list(arr):
    if (flower[0], flower[1]) <= (3, 1):
        if not res or (flower[2], flower[3]) > (res[-1][2], res[-1][3]):
            if res:
                arr.remove(res.pop())
            res = [flower]

if not res or (res[-1][2], res[-1][3]) <= (3, 1):
    print(0)
    sys.exit(0)
if (res[-1][2], res[-1][3]) > (11, 30):
    print(len(res))
    sys.exit(0)

arr.remove(res[0])

while arr:
    nxt = None
    for flower in list(arr):
        if (flower[0], flower[1]) <= (res[-1][2], res[-1][3]):
            if(flower[2], flower[3]) > (res[-1][2], res[-1][3]):
                if not nxt or (nxt[2], nxt[3]) < (flower[2], flower[3]):
                    nxt = flower
            arr.remove(flower)         
    
    if not nxt:
        break
    else:
        res.append(nxt)
    if (res[-1][2], res[-1][3]) > (11, 30):
        break
if (res[-1][2], res[-1][3]) > (11, 30):
    print(len(res))
else:
    print(0)