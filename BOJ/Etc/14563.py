import math

def f(n):
    if n == 1:
        return "Deficient"
    s = 1
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            s += i
            if i != n // i:
                s += n // i
    return "Perfect" if s == n else "Deficient" if s < n else "Abundant"

input()

for num in input().split():
    print(f(int(num)))
