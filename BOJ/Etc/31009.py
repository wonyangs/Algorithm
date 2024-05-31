import sys
input = sys.stdin.readline

N = int(input())
dic = {}
for _ in range(N):
    a, b = input().strip().split()
    dic[a] = int(b)
print(dic['jinju'])
print(len([c for c in dic.values() if c > dic['jinju']]))
