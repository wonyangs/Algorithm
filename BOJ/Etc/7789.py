import sys, math

a, b = sys.stdin.read().split()
n = int(a)
m = int(b + a)

primes = []
for x in (n, m):
    ok = x > 1
    if ok:
        if x % 2 == 0:
            ok = x == 2
        else:
            r = int(math.isqrt(x))
            for i in range(3, r + 1, 2):
                if x % i == 0:
                    ok = False
                    break
    primes.append(ok)

print('Yes' if all(primes) else 'No')
