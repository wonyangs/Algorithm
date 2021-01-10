# Solved on 2020.12.12
# 11050 이항 계수 1

ans = 1

N, K = map(int, input().split())

if K > N-K:
    K = N-K

for i in range(N, N-K, -1):
    ans *= i
for j in range(K, 0, -1):
    ans /= j

print(int(ans))
