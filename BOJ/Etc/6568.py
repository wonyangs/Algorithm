import sys

input = sys.stdin.readline


def update(adder, bit):
    b = format(adder, "b")
    if len(b) > bit:
        return int(b[-bit:], 2)
    return int(b,2)

def logic(memory):
    adder, pc = 0, 0
    
    while True:
        val = memory[pc]
        cmd, x = val[:3], int(val[3:], 2)
    
        pc += 1
        pc = update(pc, 5)
        
        if cmd == "000":
            memory[x] = format(adder, "08b")
        elif cmd == "001":
            adder = int(memory[x], 2)
        elif cmd == "010":
            if adder == 0:
                pc = x
                pc = update(pc, 5)
        elif cmd == "011":
            continue
        elif cmd == "100":
            adder -= 1
            if adder == -1:
                adder = 255
            adder = update(adder, 8)
        elif cmd == "101":
            adder += 1
            adder = update(adder, 8)
        elif cmd == "110":
            pc = x
            pc = update(pc, 5)
        elif cmd == "111":
            break
    
    # print(bin(adder)[2:].zfill(8))
    print(format(adder, "08b"))

while True:
    try:
        memory = [input().strip() for _ in range(32)]
        logic(memory)
    except Exception as e:
        break
