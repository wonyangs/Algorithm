N = int(input())
for _ in range(N):
    num = input().strip()
    if int(num[-1]) % 2 == 0:
        print("even")
    else:
        print("odd")
