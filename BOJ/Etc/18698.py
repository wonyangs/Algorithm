N = int(input())
for _ in range(N):
    s = input().strip()
    count = 0
    for c in s:
        if c == 'U':
            count += 1
        else:
            break
    print(count)
