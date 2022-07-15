# Solved on 2022. 7. 15.
# 13505 두 수 XOR

from collections import defaultdict
import sys
input = sys.stdin.readline


class TrieNode:
    def __init__(self):
        self.end = False
        self.children = defaultdict(TrieNode)


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, num):
        node = self.root
        for n in num:
            node = node.children[n]
        node.end = True
        return

    def search(self, num):
        global MAX
        node = self.root
        rev = {'0': '1', '1': '0'}
        res = []
        for n in num:
            if rev[n] in node.children.keys():
                node = node.children[rev[n]]
                res.append('1')
            elif n in node.children.keys():
                node = node.children[n]
                res.append('0')
        MAX = max(MAX, int(''.join(res), 2))


N = int(input())
nums = [*map(lambda x:format(x, 'b').rjust(32, '0'), sorted(set(map(int, input().split())), reverse=True))]
trie = Trie()
MAX = 0
for n in nums:
    trie.add(n)
for n in nums:
    trie.search(n)
print(MAX)
