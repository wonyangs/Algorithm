cnt = 0
for i in range(0, int(input()) + 1):
    cnt += str(i).count('3')
    cnt += str(i).count('6')
    cnt += str(i).count('9')
print(cnt)
