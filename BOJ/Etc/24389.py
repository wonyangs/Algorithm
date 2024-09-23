print(bin((N:=int(input())) ^ ((~N + 1) & 0xFFFFFFFF)).count('1'))
