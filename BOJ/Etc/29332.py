import sys

input = sys.stdin.readline

def solve():
    try:
        line = input().strip()
        if not line:
            return
        N = int(line)
    except ValueError:
        return

    min_x = -float('inf')
    max_x = float('inf')
    min_y = -float('inf')
    max_y = float('inf')

    for _ in range(N):
        data = input().split()
        x = int(data[0])
        y = int(data[1])
        d = data[2]

        if d == 'L': # x < x_i 이므로 최대 x는 x_i - 1
            max_x = min(max_x, x - 1)
        elif d == 'R': # x > x_i 이므로 최소 x는 x_i + 1
            min_x = max(min_x, x + 1)
        elif d == 'U': # y > y_i 이므로 최소 y는 y_i + 1
            min_y = max(min_y, y + 1)
        elif d == 'D': # y < y_i 이므로 최대 y는 y_i - 1
            max_y = min(max_y, y - 1)

    if min_x == -float('inf') or max_x == float('inf') or \
       min_y == -float('inf') or max_y == float('inf'):
        print("Infinity")
    else:
        count_x = max_x - min_x + 1
        count_y = max_y - min_y + 1
        
        print(count_x * count_y)

if __name__ == "__main__":
    solve()
