d = list(map(int, input().split()))
p = [0]
for x in d:
    p.append(p[-1] + x)

for i in range(5):
    print(*(abs(p[i] - p[j]) for j in range(5)))
