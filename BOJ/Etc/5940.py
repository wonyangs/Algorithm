a, b = map(int, input().split())
for e in range(a + 1, 63):
    if str(2 ** e)[0] == str(b):
        print(e)
        break
else:
    print(0)
