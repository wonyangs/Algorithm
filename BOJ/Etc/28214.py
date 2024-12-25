N, K, P = map(int, input().split())
bread = list(map(int, input().split()))
print(sum(bread[i*K:(i+1)*K].count(0) < P for i in range(N)))
