p = input().strip()
n = int(input())
xs = [input().strip() for _ in range(n)]
r = [x for x in xs if all(a == '*' or a == b for a, b in zip(p, x))]
print(len(r))
print(*r, sep='\n')
