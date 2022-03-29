# Solved on 2022. 3. 29.
# 5052 전화번호 목록

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
    
    def add(self, numbers):
        node = self.root
        for n in numbers:
            if node.end is True:
                return False
            node = node.children[n]
        
        if len(node.children) != 0:
            return False
        node.end = True
        return True


T = int(input())
for _ in range(T):
    N = int(input())
    trie = Trie()
    res = True
    for _ in range(N):
        num = input().strip()
        if trie.add(num) is False:
            res = False
    
    print("YES" if res else "NO")
