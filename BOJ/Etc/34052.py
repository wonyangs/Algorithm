res = 0
for _ in range(4):
    res += int(input())
print("Yes" if res + 300 <= 1800 else "No")
