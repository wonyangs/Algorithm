n = int(input())
for _ in range(n):
    stats = list(map(int, input().split()))
    print(' '.join(map(str, stats)))
    d = sum(1 for s in stats if s >= 10)
    if d == 0:
        print('zilch')
    elif d == 1:
        print('double')
    elif d == 2:
        print('double-double')
    elif d == 3:
        print('triple-double')
    print()
