J, N = map(int, input().split())
a = 0
for _ in range(N):
    s = input()
    a += sum(1 if c == ' ' else 4 if 'A' <= c <= 'Z' else 2 for c in s) <= J
print(a)
