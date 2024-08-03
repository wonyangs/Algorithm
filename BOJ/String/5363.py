from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
for _ in range(N):
    deq = deque(input().split())
    deq.rotate(-2)
    print(' '.join(deq))
