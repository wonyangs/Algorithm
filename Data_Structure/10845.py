# Solved on 2020.12.15
# 10845 큐

import sys
input = sys.stdin.readline


class Queue:
    def __init__(self):
        self.L = []

    def push(self, n):
        self.L.append(n)

    def isEmpty(self):
        if len(self.L) == 0:
            return True
        else:
            return False

    def pop(self):
        if self.isEmpty():
            print(-1)
        else:
            print(self.L[0])
            self.L = self.L[1:]

    def size(self):
        print(len(self.L))

    def empty(self):
        if self.isEmpty():
            print('1')
        else:
            print('0')

    def front(self):
        if self.isEmpty():
            print(-1)
        else:
            print(self.L[0])

    def back(self):
        if self.isEmpty():
            print(-1)
        else:
            print(self.L[-1])


n = int(input())
que = Queue()

for i in range(n):
    a = input().split()
    if a[0] == 'push':
        que.push(a[1])
    elif a[0] == 'pop':
        que.pop()
    elif a[0] == 'size':
        que.size()
    elif a[0] == 'empty':
        que.empty()
    elif a[0] == 'front':
        que.front()
    else:  # back
        que.back()
