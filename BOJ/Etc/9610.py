q1, q2, q3, q4, ax = 0, 0, 0, 0, 0
for _ in range(int(input())):
    x, y = map(int, input().split())
    if x == 0 or y == 0:
        ax += 1
    elif x > 0 and y > 0:
        q1 += 1
    elif x < 0 and y > 0:
        q2 += 1
    elif x < 0 and y < 0:
        q3 += 1
    else:
        q4 += 1

print(f'Q1: {q1}')
print(f'Q2: {q2}')
print(f'Q3: {q3}')
print(f'Q4: {q4}')
print(f'AXIS: {ax}')
