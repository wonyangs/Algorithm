# Solved on 2021. 10. 04.
# 14426 접두사 찾기

import sys
input = sys.stdin.readline


class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}


class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        current_node = self.head

        for char in string:
            if char not in current_node.children:
                current_node.children[char] = Node(char)
            current_node = current_node.children[char]
        current_node.data = string

    def search(self, string):
        current_node = self.head

        for char in string:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        return True


n, m = map(int, input().split())
trie = Trie()
result = 0

for _ in range(n):
    string = input().strip()
    trie.insert(string)
for _ in range(m):
    string = input().strip()
    if trie.search(string):
        result += 1
print(result)
