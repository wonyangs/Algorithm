for _ in range(int(input())):
    w1, w2 = input().split()
    print("Distances:", *[(ord(b) - ord(a)) % 26 for a, b in zip(w1, w2)])
