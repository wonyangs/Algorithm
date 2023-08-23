for _ in range(int(input())):
    N = int(input())
    arr = []
    for __ in range(N):
        name, drink = input().split()
        drink = int(drink)
        arr.append((drink, name))
    arr.sort()
    print(arr[-1][1])
