a = [int(input()) for _ in range(8)]
m = 0
for i in range(8):
    s = a[i] + a[(i+1) % 8] + a[(i+2) % 8] + a[(i+3) % 8]
    if s > m:
        m = s
print(m)
