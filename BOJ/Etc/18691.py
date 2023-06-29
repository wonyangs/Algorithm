T = int(input())
distances = [1, 3, 5]

for _ in range(T):
    G, C, E = map(int, input().split())
    need = max(0, E - C)
    print(distances[G - 1] * need)
