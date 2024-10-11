while (n := int(input())):
    print(min([input().strip() for _ in range(n)], key=str.lower))
