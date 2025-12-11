import sys
input = sys.stdin.readline

n = int(input())
a = [input().strip() for _ in range(n)]

for _ in range(2):
    for x in a:
        print(f"? {x}", flush=True)
        if int(input()) == 1:
            print(f"! {x}", flush=True)
            exit()
