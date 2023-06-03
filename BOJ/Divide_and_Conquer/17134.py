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


def eratos(prime):
    N = 1_000_001
    
    prime[0], prime[1] = 0, 0
    m = int(N ** 0.5)
    for i in range(2, m+1):
        if prime[i] == 1:
            for j in range(i+i, N, i):
                prime[j] = 0
            
    
N = 1_000_001
prime = [1] * N
eratos(prime)

odd_prime = prime.copy()
odd_prime[2] = 0

even_semi_prime = [0] * N
for i in range(2, N):
    if i * 2 >= N:
        break
    if prime[i] == 0:
        continue
    even_semi_prime[i * 2] = 1

conv = convolution(odd_prime, even_semi_prime)
for _ in range(int(input())):
    n = int(input())
    print(conv[n])
