# Solved on 2020.12.15
# 10866 덱

import sys
input = sys.stdin.readline


class Deque:
    def __init__(self):
        self.L = []

    def push_front(self, n):
        self.L.insert(0, n)

    def push_back(self, n):
        self.L.append(n)

    def isEmpty(self):
        if len(self.L) == 0:
            return True
        else:
            return False

    def pop_front(self):
        if self.isEmpty():
            sys.stdout.write('-1\n')
        else:
            sys.stdout.write(str(self.L[0]) + '\n')
            self.L = self.L[1:]

    def pop_back(self):
        if self.isEmpty():
            sys.stdout.write('-1\n')
        else:
            sys.stdout.write(str(self.L[-1]) + '\n')
            self.L = self.L[:-1]

    def size(self):
        sys.stdout.write(str(len(self.L)) + '\n')

    def empty(self):
        if self.isEmpty():
            sys.stdout.write('1\n')
        else:
            sys.stdout.write('0\n')

    def front(self):
        if self.isEmpty():
            sys.stdout.write('-1\n')
        else:
            sys.stdout.write(str(self.L[0]) + '\n')

    def back(self):
        if self.isEmpty():
            sys.stdout.write('-1\n')
        else:
            sys.stdout.write(str(self.L[-1]) + '\n')


n = int(input())
deq = Deque()

for i in range(n):
    a = input().split()
    if a[0] == 'push_front':
        deq.push_front(int(a[1]))
    elif a[0] == 'push_back':
        deq.push_back(int(a[1]))
    elif a[0] == 'pop_front':
        deq.pop_front()
    elif a[0] == 'pop_back':
        deq.pop_back()
    elif a[0] == 'size':
        deq.size()
    elif a[0] == 'empty':
        deq.empty()
    elif a[0] == 'front':
        deq.front()
    else:  # back
        deq.back()
