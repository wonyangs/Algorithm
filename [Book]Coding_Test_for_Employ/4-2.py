# Solved on 2020.12.30
# 4-2 시각

# ---------------------------

import sys
input = sys.stdin.readline

n = int(input())
count = 0

for hour in range(n+1):
    if hour % 10 == 3:
        count += 3600
    else:
        count += 1575  # 15 * 60 + (60-15) * 15  # 03 13 23 30~39 43 53

print(count)

