# Solved on 2020.12.21
# 2630 색종이 만들기


import sys
input = sys.stdin.readline

white = 0
blue = 0


def cut(x, y, n, L):
    global white, blue
    check = L[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if check != L[i][j]:
                cut(x, y, n//2, L)
                cut(x, y + n//2, n//2, L)
                cut(x + n//2, y, n//2, L)
                cut(x + n//2, y + n//2, n//2, L)
                return
    if check == 0:
        white += 1
        return
    else:
        blue += 1
        return


def main():
    global white, blue
    n = int(input())
    a = []

    for i in range(n):
        a.append(list(map(int, input().split())))

    cut(0, 0, n, a)
    print(white)
    print(blue)


main()
