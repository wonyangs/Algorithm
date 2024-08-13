import sys

input = sys.stdin.readline

N = int(input())
for _ in range(N):
    arr = input().strip().split()
    
    a, b, c = int(arr[0]), int(arr[2]), int(arr[4])
    op = arr[1]
    res = True
    if op == '+':
        res = a + b == c
    elif op == '-':
        res = a - b == c
    elif op == '*':
        res = a * b == c
    else:
        res = a // b == c
    print("correct" if res else "wrong answer")

        
