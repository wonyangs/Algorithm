import sys
input = sys.stdin.readline

for _ in range(int(input())):
    s = input().strip()
    res = str(int(s) + int(s[::-1]))
    print("YES" if res == res[::-1] else "NO")
