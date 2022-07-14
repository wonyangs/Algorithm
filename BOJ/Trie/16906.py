# Solved on 2022. 7. 14.
# 16906 욱제어

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

    def add(self, word):
        node = self.root
        for w in word:
            node = node.children[w]
        node.end = True
        return

    def can_put(self, depth):
        node = self.root
        res = []
        self.DFS(depth, node, res)
        return res

    def DFS(self, depth, node, res):
        if node.end is True:
            return False
        if depth == 0:
            if len(node.children.keys()) == 0:
                return True
            return False
        for n in [0, 1]:
            res.append(n)
            if self.DFS(depth - 1, node.children[n], res) is True:
                return True
            res.pop()
        return False


N = int(input())
word_len = [*map(int, input().split())]
res = []

trie = Trie()
for ln in word_len:
    word = trie.can_put(ln)
    if len(word) == ln:
        trie.add(word)
        res.append(''.join([*map(str, word)]))
    else:
        break
if len(res) != N:
    print(-1)
else:
    print(1)
    for word in res:
        print(word)
