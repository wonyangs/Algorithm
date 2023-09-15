import sys
input = sys.stdin.readline

s = {
    "Never gonna give you up",
"Never gonna let you down",
"Never gonna run around and desert you",
"Never gonna make you cry",
"Never gonna say goodbye",
"Never gonna tell a lie and hurt you",
"Never gonna stop"
}

N = int(input())
cnt = 0
for _ in range(N):
    if input().strip() in s:
        cnt += 1
if N != cnt:
    print("Yes")
else:
    print("No")
