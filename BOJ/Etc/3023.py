r, c = map(int, input().split())
q = [input() for _ in range(r)]
a, b = map(int, input().split())

t = [s + s[::-1] for s in q]
t += t[::-1]

l = list(t[a - 1])
l[b - 1] = '#' if l[b - 1] == '.' else '.'
t[a - 1] = ''.join(l)

print("\n".join(t))
