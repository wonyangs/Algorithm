n = int(input())
s = input().strip()
print("Yes" if all(s[i] != s[i + 1] for i in range(1, 2 * n - 1, 2)) else "No")
