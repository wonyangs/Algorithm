i = 1
while True:
    n, *data = map(int, input().split())
    if n == 0:
        break
    if n % 2 == 1:
        median = data[n//2 - 1]
    else:
        median = (data[n//2 - 1] + data[n//2]) / 2
    print(f'Case {i}: {median:.1f}')
    i += 1
