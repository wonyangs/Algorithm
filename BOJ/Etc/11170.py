for _ in range(int(input())):
    N, M = map(int, input().split())
    
    zero = 0
    for i in range(N, M+1):
        zero += str(i).count('0')
    print(zero)
