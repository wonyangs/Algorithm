from itertools import combinations as c

d = [int(input()) for _ in range(9)]

for x in c(d, 7):
    if sum(x) == 100:
        for n in sorted(x):
            print(n)
        break
