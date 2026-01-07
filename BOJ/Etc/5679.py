while True:
    try:
        n = int(input())
    except:
        break
    if n == 0:
        break
    
    m = n
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        m = max(m, n)
    print(m)
