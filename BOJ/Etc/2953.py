# Solved on 2022. 6. 9.
# 2953 나는 요리사다

import sys

arr = []
for i in range(1, 6):
    arr.append((i, sum(map(int, input().split()))))
arr.sort(key=lambda x:x[1], reverse=True)
print(*arr[0])

