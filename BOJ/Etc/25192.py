import sys
input = sys.stdin.readline

hello = set()
cnt = 0
for _ in range(int(input())):
    user = input().strip()
    if user == "ENTER":
        hello = set()
    elif user not in hello:
        cnt += 1
        hello.add(user)
print(cnt)
