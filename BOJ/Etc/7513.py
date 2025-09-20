t = int(input())
for c in range(1, t + 1):
    m = int(input())
    w = [input() for _ in range(m)]
    n = int(input())
    print(f"Scenario #{c}:")
    for _ in range(n):
        l = list(map(int, input().split()))
        print("".join(w[l[i]] for i in range(1, l[0] + 1)))
    if c < t:
        print()
