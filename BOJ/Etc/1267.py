n = int(input())
times = list(map(int, input().split()))

y_cost = sum((t // 30 + 1) * 10 for t in times)
m_cost = sum((t // 60 + 1) * 15 for t in times)

if y_cost < m_cost:
    print(f"Y {y_cost}")
elif y_cost > m_cost:
    print(f"M {m_cost}")
else:
    print(f"Y M {y_cost}")
