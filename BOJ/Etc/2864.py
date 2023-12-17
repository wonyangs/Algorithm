import sys
input = sys.stdin.readline

A, B = input().strip().split()

def func(dest, src):
    return int(A.replace(dest, src)) + int(B.replace(dest, src))

print(func('6', '5'), func('5', '6'))
