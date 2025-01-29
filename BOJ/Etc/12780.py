H = input().strip()
N = input().strip()

count = 0
for i in range(len(H) - len(N) + 1):
    if H[i:i+len(N)] == N:
        count += 1

print(count)
