# Solved on 2022. 7. 13.
# 16934 게임 닉네임

from collections import defaultdict
import sys
input = sys.stdin.readline


class TrieNode:
    def __init__(self):
        self.end = 0
        self.children = defaultdict(TrieNode)


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, nickname):
        find = False
        node = self.root
        for n in nickname:
            if not find:
                print(n, end='')
            if not find and n not in node.children.keys():
                find = True
            node = node.children[n]

        if node.end != 0:
            print(node.end + 1, end='')
        print()
        node.end += 1
        return True


N = int(input())
trie = Trie()
for _ in range(N):
    nickname = input().strip()
    trie.add(nickname)
