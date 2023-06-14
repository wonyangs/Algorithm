depth = 0
while True:
    try:
        line = input().split()
        if line[0] == 'Es':
            depth += int(line[1]) * 21
        elif line[0] == 'Stair':
            depth += int(line[1]) * 17
    except EOFError:
        break
print(depth)
