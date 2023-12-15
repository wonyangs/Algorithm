res = float(input())
while True:
    N = float(input())
    if N == 999:
        break
    print("%.2f"%(N - res))
    res = N
