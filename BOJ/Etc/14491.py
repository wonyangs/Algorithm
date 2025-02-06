n=int(input())
s=''
while n:
    s = str(n % 9) + s
    n //= 9
print(s or 0)
