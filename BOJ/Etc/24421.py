n = int(input())
a = list(map(int, input().split()))
c = 0
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if a[i] * a[j] == a[k]:
                c += 1
print(c)
