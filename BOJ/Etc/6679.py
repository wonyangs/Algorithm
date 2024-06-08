def digit_sum(n, base):
    sum_digits = 0
    while n > 0:
        sum_digits += n % base
        n //= base
    return sum_digits

def find_singihan_numbers():
    results = []
    for num in range(1000, 10000):
        sum_10 = digit_sum(num, 10)
        sum_12 = digit_sum(num, 12)
        sum_16 = digit_sum(num, 16)
        if sum_10 == sum_12 == sum_16:
            results.append(num)
    return results

singihan_numbers = find_singihan_numbers()
for number in singihan_numbers:
    print(number)
