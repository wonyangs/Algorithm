# Solved on 2022. 3. 30.
# 14725 개미굴

from collections import defaultdict
import sys
input = sys.stdin.readline

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def add(self, names):
        node = self.root
        for n in names:
            node = node.children[n]
    
    def travel(self, depth, node):
        if len(node.children) == 0:
            return
        
        for n in sorted(node.children):
            print("--"*depth + n)
            self.travel(depth+1, node.children[n])


T = int(input())
trie = Trie()
for _ in range(T):
    N, *arr  = input().split()
    trie.add(arr)
trie.travel(0, trie.root)
