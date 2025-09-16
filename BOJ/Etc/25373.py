n = int(input())
if n <= 28:
    for i in range(1, 8):
        if n <= sum(range(1, i + 1)):
            print(i)
            break
else:
    print((n - 29) // 7 + 8)
