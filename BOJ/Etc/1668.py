N = int(input())
T = [int(input()) for _ in range(N)]
f = lambda L: sum(x > max(L[:i]) if i > 0 else 1 for i, x in enumerate(L))
print(f(T), f(T[::-1]))
