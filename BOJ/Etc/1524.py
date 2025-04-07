import sys
input_data = sys.stdin.read().strip().split()
t = int(input_data[0])
idx = 1
for _ in range(t):
    ns = int(input_data[idx])
    idx += 1
    ms = int(input_data[idx])
    idx += 1
    s = list(map(int, input_data[idx:idx+ns]))
    idx += ns
    b = list(map(int, input_data[idx:idx+ms]))
    idx += ms
    ps = max(s)
    pb = max(b)
    if ps > pb:
        print("S")
    elif ps < pb:
        print("B")
    else:
        x = s.count(ps)
        y = b.count(pb)
        if x >= y:
            print("S")
        else:
            print("B")
