N = int(input()) - 1
print(chr(0xAC00 + 28*21*(N//(21*28)) + 28*((N%(21*28))//28) + N%28))
