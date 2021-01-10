# Solved on 2021. 01. 09
# 6-3 성적이 낮은 순서로 학생 출력하기

import sys
input = sys.stdin.readline

n = int(input())
array = []

for _ in range(n):
    input_data = input().split()
    array.append((input_data[0], int(input_data[1])))

array.sort(key=lambda student: student[1])

for student in array:
    print(student[0], end=' ')
