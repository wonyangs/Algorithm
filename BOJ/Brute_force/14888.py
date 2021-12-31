# Solved on 2021. 10. 28.
# 14888 연산자 끼워넣기

from itertools import permutations, combinations
import sys
input = sys.stdin.readline


def calculate(nums, opers):
    res = nums[0]

    for i in range(N-1):
        op = opers[i]
        n = nums[i+1]

        if op == '+':
            res += n
        elif op == '-':
            res -= n
        elif op == '*':
            res *= n
        elif op == '/':
            if res > 0:
                res //= n
            else:
                res *= -1
                res //= n
                res *= -1
        else:
            print('oper error')

    return res


N = int(input())
nums = list(map(int, input().split()))

oper = []
operText = ['+', '-', '*', '/']
operNum = list(map(int, input().split()))
for i in range(4):
    for _ in range(operNum[i]):
        oper.append(operText[i])
        
comNums = list(combinations(nums, N))
setOper = set(permutations(oper, N-1))
comOper = [n for n in setOper]

arr = []
for numList in comNums:
    for operList in comOper:
        res = calculate(numList, operList)
        arr.append(res)

print(max(arr))
print(min(arr))
