X = int(input())
n = 1
while X > n: X -= n; n += 1
print(f"{X}/{n-X+1}" if n % 2 == 0 else f"{n-X+1}/{X}")
