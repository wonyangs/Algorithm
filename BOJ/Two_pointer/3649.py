# Solved on 2022. 6. 14.
# 3649 로봇 프로젝트

import sys
input = sys.stdin.readline

while True:
    try:
        x = int(input())
        n = int(input())

        arr = sorted([int(input()) for _ in range(n)])

        i = 0
        j = n - 1
        while i < j:
            if arr[i] + arr[j] == x * 10000000:
                print("yes %d %d" %(arr[i], arr[j]))
                break

            if arr[i] + arr[j] < x * 10000000:
                i += 1
            else:
                j -= 1
        if not i < j:
            print("danger")
    except:
        break
