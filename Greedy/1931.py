# Solved on 2021. 01. 10.
# 1931 회의실 배정

import sys
input = sys.stdin.readline


n = int(input())
plan = []

for _ in range(n):
    input_data = input().split()
    plan.append((int(input_data[0]), int(input_data[1])))


plan.sort(key=lambda x: x[0])
plan.sort(key=lambda x: x[1])
print(plan)
count = 0
start_time = 0

for time in plan:
    if time[0] >= start_time:
        start_time = time[1]
        count += 1

print(count)
