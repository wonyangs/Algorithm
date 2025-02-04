for _ in range(int(input())):
    M, t = input().split()
    print(" ".join(str(ord(x) - 64) if t == 'C' else chr(int(x) + 64) for x in input().split()))
