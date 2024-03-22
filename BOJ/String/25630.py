N = int(input())
s = input()

cnt = 0
for i in range(0, N//2):
    if s[i] != s[-i-1]:
        cnt+=1
        
print(cnt)
