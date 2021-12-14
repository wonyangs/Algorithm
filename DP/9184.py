# Solved on 2021. 12. 14.
# 9184 신나는 함수 실행

import sys
input = sys.stdin.readline

def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif dp[a][b][c] != -1:
        return dp[a][b][c]

    if a > 20 or b > 20 or c > 20:
        dp[a][b][c] = w(20, 20, 20)
    elif a < b and b < c:
        dp[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
    else:
        dp[a][b][c] =  w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    return dp[a][b][c]

N = 51
dp = [[[-1] * N for _ in range(N)] for _ in range(N)]
while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    print(f'w({a}, {b}, {c}) = {w(a, b, c)}')
