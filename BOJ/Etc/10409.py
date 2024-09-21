n, T, *times = map(int, input().split() + input().split())
total = count = 0
for t in times:
    if (total := total + t) > T: break
    count += 1
print(count)
