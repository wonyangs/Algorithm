# Solved on 2022. 3. 4.
# 11729 하노이 탑 이동 순서

import sys
input = sys.stdin.readline

def left_place(a, b):
    arr = [1, 2, 3]
    arr.remove(a)
    arr.remove(b)
    return arr[0]

def hano(n, now, target):
    global block, count
    if n == 0:
        return
    left = left_place(block[n], target)
    hano(n-1, block[n-1], left)
    log.append((block[n], target))
    block[n] = target
    count += 1
    hano(n-1, block[n-1], target)


N = int(input())
block = [1] * (N+1)
count = 0
log = []
hano(N, 1, 3)
print(count)
for l in log:
    print(*l)
