while True:
    numbers = list(map(int, input().split()))
    if numbers[0] == -1:
        break
    numbers.pop()
    count = sum(1 for x in numbers if 2 * x in numbers)
    print(count)
