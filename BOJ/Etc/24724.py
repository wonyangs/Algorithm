import sys
input = sys.stdin.readline

T = int(input())
for x in range(1, T + 1):
    N = int(input())
    A, B = map(int, input().split())
    for _ in range(N):
        input()
    print(f"Material Management {x}")
    print("Classification ---- End!")
