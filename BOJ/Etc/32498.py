n = int(input())
cnt = 0
for _ in range(n):
    if (i := int(input())) % 2 != 0:
        cnt += 1
        
print(cnt)
