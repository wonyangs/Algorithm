for i in range(int(input())):
    print(f"String #{i+1}\n{''.join(chr((ord(c)-64)%26+65) for c in input())}\n")
