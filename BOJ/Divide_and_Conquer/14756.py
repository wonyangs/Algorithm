import cmath
import sys

input = sys.stdin.readline

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


N, L, M, W = map(int, input().split())
A = [[*map(int, input().split())] for _ in range(M)]
B = [[*map(int, input().split())] for _ in range(M)]

res = []
for i in range(M):
    conv = convolution(A[i], list(reversed(B[i])))
    res.append(conv[L-1:N])

col_sum = [sum(col) for col in zip(*res)]

print(len([n for n in col_sum if n > W]))
