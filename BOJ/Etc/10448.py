t = int(input())
k = [int(input()) for _ in range(t)]

def tri(n):
    return n * (n + 1) // 2

tri_nums = [tri(i) for i in range(1, 45)]
s = set(tri_nums)

for x in k:
    found = 0
    for i in tri_nums:
        for j in tri_nums:
            if x - i - j in s:
                found = 1
                break
        if found:
            break
    print(found)
