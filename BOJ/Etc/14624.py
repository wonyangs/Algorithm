N = int(input())

if N % 2 == 0:
    print("I LOVE CBNU")
else:
    print("*" * N)
    
    mid = N // 2
    print(" " * mid + "*")
    
    for i in range(mid):
        print(" " * (mid - 1 - i) + "*" + " " * (2 * i + 1) + "*")
