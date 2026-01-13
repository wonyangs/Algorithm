l = list(map(int, input().split()))
c = 0
for i in range(5):
    for j in range(i + 1, 5):
        for k in range(j + 1, 5):
            t = [l[i], l[j], l[k]]
            if sum(t) - max(t) > max(t):
                c += 1
print(c)
