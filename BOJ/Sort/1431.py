import sys
input = sys.stdin.readline

def numsum(x):
    res = 0
    for i in x:
        if i.isdigit():
            res += int(i)
    return res

arr = [input().strip() for _ in range(int(input()))]
arr.sort(key=lambda x:(len(x), numsum(x), x))
print(*arr, sep='\n')
