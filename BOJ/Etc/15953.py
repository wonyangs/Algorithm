first = [0, 5000000] + [3000000]*2 + [2000000]*3 + [500000]*4 + [300000]*5 + [100000]*6 + [0]*79
second = [0, 5120000] + [2560000]*2 + [1280000]*4 + [640000]*8 + [320000]*16 + [0]*33

for _ in range(int(input())):
    a, b = map(int, input().split())
    print(first[a] + second[b])
