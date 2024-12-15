for t in range(1, int(input()) + 1):
    a, b, c = sorted(map(int, input().split()))
    print(f"Case #{t}: {'invalid!' if a + b <= c else 'equilateral' if a == c else 'isosceles' if a == b or b == c else 'scalene'}")
