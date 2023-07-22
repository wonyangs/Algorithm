import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dic = dict()
for _ in range(N):
    key, value = input().strip().split()
    dic[key] = value
for _ in range(M):
    print(dic[input().strip()])
