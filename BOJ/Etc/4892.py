i = 1

while True:
    n = int(input())
    if n == 0:
        break

    n1 = 3 * n

    if n1 % 2 == 0:
        parity = "even"
        n2 = n1 // 2
    else:
        parity = "odd"
        n2 = (n1 + 1) // 2

    n3 = 3 * n2
    n4 = n3 // 9

    print(f"{i}. {parity} {n4}")
    i += 1
