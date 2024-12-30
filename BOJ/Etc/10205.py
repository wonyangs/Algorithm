K = int(input())
for k in range(1, K + 1):
    h = int(input())
    for a in input():
        h += 1 if a == 'c' else -1
        if h <= 0: h = 0; break
    print(f"Data Set {k}:\n{h}\n")
