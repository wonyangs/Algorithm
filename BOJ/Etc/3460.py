print('\n'.join(' '.join(str(i) for i, bit in enumerate(bin(int(input()))[2:][::-1]) if bit == '1') for _ in range(int(input()))))
