while True:
    a, b = map(int, input().split())
    if a == b == 0:
        break
    
    carry = [0]
    while a > 0 or b > 0:
        mod_a, mod_b = a % 10, b % 10
        if mod_a + mod_b + carry[-1] > 9:
            carry.append(1)

        a //= 10
        b //= 10
    
    print(sum(carry))
