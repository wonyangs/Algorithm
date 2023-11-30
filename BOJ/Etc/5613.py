num = int(input())
while True:
    op = input()
    if op == '=':
        print(num)
        break
    
    nxt = int(input())
    if op == '+':
        num += nxt
    elif op == '-':
        num -= nxt
    elif op == '*':
        num *= nxt
    elif op == '/':
        num /= nxt
        num = int(num)
