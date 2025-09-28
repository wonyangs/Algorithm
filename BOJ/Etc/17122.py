t = int(input())
for _ in range(t):
    s1, s2 = input().split()
    c1 = ord(s1[0]) - ord('A') + 1
    r1 = int(s1[1])
    n = int(s2)
    r2 = (n - 1) // 8 + 1
    c2 = (n - 1) % 8 + 1
    if (c1 + r1) % 2 == (c2 + r2) % 2:
        print("YES")
    else:
        print("NO")
