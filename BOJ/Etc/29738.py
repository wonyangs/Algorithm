T = int(input())
for t in range(1, T + 1):
    N = int(input())
    r = "World Finals" if N <= 25 else "Round 3" if N <= 1000 else "Round 2" if N <= 4500 else "Round 1"
    print(f"Case #{t}: {r}")
