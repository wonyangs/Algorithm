import math

case = 1
while True:
    a, b, c = map(float, input().split())
    if not any([a, b, c]): break
    print(f"Triangle #{case}")
    
    if a == -1 and c ** 2 > b ** 2:
        print(f"a = {math.sqrt(c ** 2 - b ** 2):.3f}")
    elif b == -1 and c ** 2 > a ** 2:
        print(f"b = {math.sqrt(c ** 2 - a ** 2):.3f}")
    elif c == -1:
        print(f"c = {math.sqrt(a ** 2 + b ** 2):.3f}")
    else:
        print("Impossible.")
    
    print()
    case += 1
