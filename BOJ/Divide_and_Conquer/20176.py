import cmath

def fft(a, inv=False):
    n = len(a)
    b = a.copy()
    
    for i in range(n):
        sz = n
        shift = 0
        idx = i
        while sz > 1:
            if idx & 1:
                shift += sz >> 1
            idx >>= 1
            sz >>= 1
        a[shift + idx] = b[i]

    i = 1
    while i < n:
        x = cmath.pi / i if inv else -cmath.pi / i
        w = cmath.cos(x) + cmath.sin(x) * 1j

        for j in range(0, n, i << 1):
            th = 1 + 0j
            for k in range(i):
                tmp = a[i + j + k] * th
                a[i + j + k] = a[j + k] - tmp
                a[j + k] += tmp
                th *= w
        i <<= 1

    if inv:
        for i in range(n):
            a[i] /= n


def convolution(a, b):
    N = 1
    while N < len(a) + len(b):
        N *= 2
    
    a += [complex(0)] * (N - len(a))
    b += [complex(0)] * (N - len(b))
    
    fft(a, False)
    fft(b, False)
    
    c = [a[i] * b[i] for i in range(N)]
    fft(c, True)
    for i, n in enumerate(c):
        c[i] = round(c[i].real)
    return c


N = int(input())
a = [*map(int, input().split())]
N = int(input())
b = [*map(int, input().split())]
N = int(input())
c = [*map(int, input().split())]


na = [0] * 60001
nb = [0] * 60001
nc = [0] * 60001

for i in a:
    na[i + 30000] += 1
for i in b:
    nb[i + 30000] += 1
for i in c:
    nc[i + 30000] += 1

conv = convolution(na, nc)

res = 0
for i in range(0, 60001):
    res += nb[i] * conv[2*i]

print(res)
