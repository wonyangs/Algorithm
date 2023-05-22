for _ in range(int(input())):
    id, s, m, t = map(int, input().split())
    total = s + m + t
    print(id, total, 'PASS' if s >= 10.5 and m >= 7.5 and t >= 12 and total >= 55 else 'FAIL')
