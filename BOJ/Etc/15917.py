import sys
input=sys.stdin.readline

for _ in range(int(input())):
    a = int(input())
    while a % 2 == 0:
        a //= 2
    print(1 if a == 1 else 0)
