# Solved on 2021. 11. 14.
# 1963 소수 경로

from collections import deque
import sys
input = sys.stdin.readline


def changeNum(n):
    res = []
    arr = []
    for _ in range(4):
        arr.append(n % 10)
        n //= 10
    arr.reverse()

    for i in range(4):
        tmp = arr[i]
        for j in range(0, 10):
            if i == 0 and j == 0:
                continue
            if j == tmp:
                continue
            arr[i] = j
            num = 0
            for k in range(4):
                num *= 10
                num += arr[k]
            if num in primeNum:
                res.append(num)
        arr[i] = tmp
    return res


def bfs(start, end):
    queue = deque()
    queue.append(start)
    visit = [-1] * 10000
    visit[start] = 0

    while queue:
        n = queue.popleft()
        if n == end:
            break

        arr = changeNum(n)
        for num in arr:
            if visit[num] == -1:
                visit[num] = visit[n] + 1
                queue.append(num)

    if visit[end] == -1:
        print('Impossible')
    else:
        print(visit[end])


prime = []
for i in range(2, 10000):
    isPrime = True
    for p in prime:
        if i % p == 0:
            isPrime = False
            break
    if isPrime:
        prime.append(i)

primeNum = set()
for n in prime:
    if n >= 1000:
        primeNum.add(n)

T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    bfs(a, b)
