for _ in range(int(input())):
    car = int(input())
    for __ in range(int(input())):
        n, op = map(int, input().split())
        car += n * op
    print(car)
