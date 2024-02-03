n, m, k = map(int, input().split())
i = 1
while (k-m)*i < n:
    i+=1
print(i)
