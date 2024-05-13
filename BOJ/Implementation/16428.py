A, B = map(int, input().split())

quotient = A // B
remainder = A % B

if remainder < 0:
    if B > 0:
        remainder += B
        quotient -= 1
    else:
        remainder -= B
        quotient += 1

print(quotient)
print(remainder)
