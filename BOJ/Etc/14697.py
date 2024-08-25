A, B, C, N = map(int, input().split())
print(1 if any((N - x * A) % B == 0 or (N - x * A) % C == 0 or (N - x * A - y * B) % C == 0 for x in range(N // A + 1) for y in range((N - x * A) // B + 1)) else 0)
