T = int(input())
for _ in range(T):
    input_str, output_str = input().split()
    if input_str == output_str:
        print('OK')
    else:
        print('ERROR')
