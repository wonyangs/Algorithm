for _ in range(int(input())):
    n = int(input())
    res = ""
    res += "++++ " * (n//5)
    res += "|" * (n%5)
    print(res.strip())
