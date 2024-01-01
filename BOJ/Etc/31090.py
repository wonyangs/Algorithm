for _ in range(int(input())):
    N = int(input())
    print("Good" if (N + 1) % (N % 100) == 0 else "Bye")
