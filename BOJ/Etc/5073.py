while True:
    sides = list(map(int, input().split()))
    if sum(sides) == 0:
        break
    max_side = max(sides)
    sides.remove(max_side)
    if max_side >= sum(sides):
        print("Invalid")
    elif len(set(sides + [max_side])) == 1:
        print("Equilateral")
    elif len(set(sides + [max_side])) == 2:
        print("Isosceles")
    else:
        print("Scalene")
