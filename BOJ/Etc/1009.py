import sys
input = sys.stdin.readline

def find_last_computer(T, test_cases):
    results = []
    for a, b in test_cases:
        a = a % 10
        
        cycles = {
            0: [0],
            1: [1],
            2: [2, 4, 8, 6],
            3: [3, 9, 7, 1],
            4: [4, 6],
            5: [5],
            6: [6],
            7: [7, 9, 3, 1],
            8: [8, 4, 2, 6],
            9: [9, 1]
        }
        
        cycle = cycles[a]
        cycle_length = len(cycle)
        
        index = (b - 1) % cycle_length
        last_digit = cycle[index]
        
        results.append(10 if last_digit == 0 else last_digit)
    return results


T = int(input())
test_cases = []
for _ in range(T):
    a, b = map(int, input().split())
    test_cases.append((a, b))

results = find_last_computer(T, test_cases)
for result in results:
    print(result)
