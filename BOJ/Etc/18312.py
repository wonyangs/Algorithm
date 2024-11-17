N, K = input().split()
print(sum(K in f"{h:02}{m:02}{s:02}" for h in range(int(N)+1) for m in range(60) for s in range(60)))
