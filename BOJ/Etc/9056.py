for _ in range(int(input())):
    a, b = input().split()
    print("YES" if set(a) == set(b) else "NO")
