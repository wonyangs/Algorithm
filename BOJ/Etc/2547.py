for _ in range(int(input())):
    input()
    N = int(input())
    print("YES" if sum(int(input()) for _ in range(N)) % N == 0 else "NO")
