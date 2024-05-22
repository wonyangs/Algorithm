s = input()[:5]
cnt = 0
for _ in range(int(input())):
    if s == input()[:5]:
        cnt += 1
print(cnt)
