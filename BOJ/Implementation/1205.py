import sys

input = sys.stdin.readline

N, my_score, M = map(int, input().split())
if N == 0:
    print(1)
    sys.exit()

arr = [*map(int, input().split())]

if N == M and my_score == arr[-1]:
    print(-1)
    sys.exit()
if N != M and my_score < arr[-1]:
    print(N + 1)
    sys.exit()

prev_score = -1
now_rank = 1
my_rank = -1
for i, n in enumerate(arr, 1):
    if prev_score != n:
        now_rank = i
        prev_score = n
    
    if n <= my_score:
        my_rank = now_rank
        break

print(my_rank)
