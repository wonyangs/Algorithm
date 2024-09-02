N = int(input())
while any(c not in '47' for c in str(N)): N -= 1
print(N)
