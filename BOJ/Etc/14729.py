import sys
input = sys.stdin.readline

arr = [float(input()) for _ in range(int(input()))]
arr.sort()
for f in arr[:7]:
    print("%.3f"%f)
