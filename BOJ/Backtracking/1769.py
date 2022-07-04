# Solved on 2022. 7. 4.
# 1769 3의 배수

import sys
input = sys.stdin.readline

def recursion(n, cnt):
    if len(str(n)) == 1:
        print(cnt)
        if n % 3 == 0:
            print("YES")
        else:
            print("NO")
        return
    
    return recursion(sum([*map(int, str(n))]), cnt + 1)

recursion(int(input()), 0)
