from collections import deque


S = input()
T = input()

res = 0

deq = deque(T)

while len(deq) != len(S):
    if deq[-1] == 'A':
        deq.pop()
    else:
        deq.pop()
        deq.reverse()

print(1 if ''.join(deq) == S else 0)
