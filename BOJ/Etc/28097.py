N = int(input())
T = list(map(int, input().split()))

total_time = sum(T) + (N - 1) * 8

days = total_time // 24
hours = total_time % 24

print(days, hours)
