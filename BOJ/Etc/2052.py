from decimal import Decimal, getcontext

n = int(input())
getcontext().prec = 300
x = Decimal(1) / (Decimal(2) ** n)
s = format(x, 'f').rstrip('0').rstrip('.')
print(s if s else '0')
