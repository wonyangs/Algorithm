G_SCORES = [1, 2, 3, 3, 4, 10]
S_SCORES = [1, 2, 2, 2, 3, 5, 10]

T = int(input())
results = []

for i in range(T):
    G_army = list(map(int, input().split()))
    S_army = list(map(int, input().split()))
    
    G_total = sum(g * s for g, s in zip(G_army, G_SCORES))
    S_total = sum(s * t for s, t in zip(S_army, S_SCORES))
    
    if G_total > S_total:
        results.append(f"Battle {i + 1}: Good triumphs over Evil")
    elif G_total < S_total:
        results.append(f"Battle {i + 1}: Evil eradicates all trace of Good")
    else:
        results.append(f"Battle {i + 1}: No victor on this battle field")

for result in results:
    print(result)
