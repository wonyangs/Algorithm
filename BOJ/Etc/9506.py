while True:
    n = int(input())
    if n == -1:
        break
    d = [i for i in range(1, n) if n % i == 0]
    if sum(d) == n:
        print(f"{n} = {' + '.join(map(str, d))}")
    else:
        print(f"{n} is NOT perfect.")
