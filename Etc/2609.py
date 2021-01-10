# Solved on 2020.12.13
# 2609 최대공약수와 최소공배수


def GCD(a, b):
    if b == 0:
        return a
    else:
        return GCD(b, a % b)


a, b = map(int, input().split())

d = GCD(a, b)

print(d, int(a * b / d), end='\n')
