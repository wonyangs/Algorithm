N, K = map(int, input().split())
temps = list(map(int, input().split()))
print(max(sum(temps[i:i+K]) for i in range(N-K+1)))
