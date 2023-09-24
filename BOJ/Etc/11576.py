A, B = map(int, input().split())
m = int(input())
nums = list(map(int, input().split()))

num_10 = 0
for i in range(m):
    num_10 += nums[i] * (A ** (m - i - 1))

num_B = []
while num_10 > 0:
    num_B.append(str(num_10 % B))
    num_10 //= B

print(' '.join(num_B[::-1]))
