# Solved on 2020.12.16
# 11723 집합


import sys
input = sys.stdin.readline


class Set():
    def __init__(self):
        self.S = set()

    def isIn(self, x):
        if x in self.S:
            return True
        else:
            return False

    def add(self, x):
        self.S.add(x)

    def remove(self, x):
        self.S.discard(x)

    def check(self, x):
        if self.isIn(x):
            sys.stdout.write('1\n')
        else:
            sys.stdout.write('0\n')

    def toggle(self, x):
        if self.isIn(x):
            self.remove(x)
        else:
            self.add(x)

    def s_all(self):
        self.S = set(i+1 for i in range(20))

    def empty(self):
        self.S.clear()


def main():
    M = int(input())
    S = Set()
    for _ in range(M):
        a = input().split()
        cmd = a[0]
        if len(a) == 2:
            x = int(a[1])

        if cmd == 'add':
            S.add(x)
        elif cmd == 'remove':
            S.remove(x)
        elif cmd == 'check':
            S.check(x)
        elif cmd == 'toggle':
            S.toggle(x)
        elif cmd == 'all':
            S.s_all()
        else:  # cmd == 'empty'
            S.empty()


main()

