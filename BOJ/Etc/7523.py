t = int(input())
for i in range(1, t + 1):
    n, m = map(int, input().split())
    s = (n + m) * (m - n + 1) // 2
    print(f"Scenario #{i}:\n{s}\n")
