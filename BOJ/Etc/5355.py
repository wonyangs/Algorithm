T = int(input())
for _ in range(T):
    parts = input().split()
    value = float(parts[0])
    for op in parts[1:]:
        value = value * 3 if op == '@' else value + 5 if op == '%' else value - 7
    print(f"{value:.2f}")
