S = int(input())
A = int(input())
B = int(input())
cost = 250
height = A
while height < S:
    height += B
    cost += 100
print(cost)
