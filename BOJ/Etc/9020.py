prime_set = set()

for n in range(2, 10001):
    for i in prime_set:
        if n % i == 0:
            break
    else:
        prime_set.add(n)

def is_prime(n):
    return n in prime_set

for _ in range(int(input())):
    N = int(input())
    a, b = N // 2, N // 2
    while a != 0:
        if is_prime(a) is True and is_prime(b) is True:
            print(a, b)
            break
        else:
            a -= 1
            b += 1
