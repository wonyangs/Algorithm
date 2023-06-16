r1, r2 = map(int, input().split())
n = int(input())
for _ in range(n):
    u = int(input())
    b = u * r1 if u <= 1000 else 1000 * r1 + (u - 1000) * r2
    print(f'{u} {b}')
