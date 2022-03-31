# Solved on 2022. 3. 31.
# 5670 휴대폰 자판

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
    
    def add(self, string):
        node = self.root
        for c in string:
            node = node.children[c]
        node.end = True
    
    def search(self, string):
        count = 0
        node = self.root
        for i in range(len(string)):
            if i == 0 or (node.end or len(node.children) != 1):
                count += 1
            node = node.children[string[i]]
        return count

while True:
    try:
        N = int(input())
        arr = [input().strip() for _ in range(N)]
        trie = Trie()
        for string in arr:
            trie.add(string)
        
        count = 0
        for string in arr:
            count += trie.search(string)
        print("%.2f"%(count/N))

    except:
        break
