while True:
    N = int(input())
    if N == 0:
        break
    print("PREMIADO" if N % 42 == 0 else "TENTE NOVAMENTE")
