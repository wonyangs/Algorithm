a = int(input())
x = int(input())
b = int(input())
y = int(input())
T = int(input())

total_minutes = T * 21

cost_1 = a + max(0, total_minutes - 30*21) * x
cost_2 = b + max(0, total_minutes - 45*21) * y

print(cost_1, cost_2)
