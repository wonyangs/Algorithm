for _ in range(int(input())):
    a, b = [sorted(map(int, input().split()[1:]), reverse=True) for _ in range(2)]
    print("AB"[a < b] if a != b else "D")
