n = int(input())
w = [input().strip() for _ in range(n)]
for x in w:
    if x[::-1] in w:
        print(len(x), x[len(x)//2])
        break
