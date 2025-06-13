n, r, c = map(int, input().split())
for i in range(1, n + 1):
    row = ''
    for j in range(1, n + 1):
        if (i + j) % 2 == (r + c) % 2:
            row += 'v'
        else:
            row += '.'
    print(row)
