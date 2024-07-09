N, L = input().split()
N = int(N)
L_str = str(L)

i = 1
while N:
    if L_str not in str(i):
        N -= 1
    i += 1
print(i-1)
