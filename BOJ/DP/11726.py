# Solved on 2020.12.22
# 11726 2×n 타일링

# ---------------------------

import sys
input = sys.stdin.readline


def main():
    a = [1, 2]

    n = int(input())
    for i in range(n-2):
        a.append(sum(a[-2:]))
    print(a[n-1] % 10007)


main()
