a = int(input())

first_ratio = 1
if a != 0:
    first_ratio = 100 / a

second_ratio = 1
if a != 100:
    second_ratio = 100 / (100 - a)

print(first_ratio)
print(second_ratio)
