n = int(input())
for i in range(n):
    print(f"Case #{i+1}: {' '.join(input().split()[::-1])}")
