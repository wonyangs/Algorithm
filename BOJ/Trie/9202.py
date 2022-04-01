# Solved on 2022. 4. 1.
# 9202 Boggle

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
        for c in word:
            node = node.children[c]
        node.end = True
    
    def check(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        
        return node

def dfs(graph, x, y, arr, res, visit, node):
    dx, dy = [-1, -1, -1, 0, 0, 1, 1, 1], [-1, 0, 1, -1, 1, -1, 0, 1]
    for i in range(8):
        nx, ny = x+dx[i], y+dy[i]
        if nx < 0 or nx >= 4 or ny < 0 or ny >= 4 or (nx, ny) in visit:
            continue
        if graph[nx][ny] in node.children:
            if node.children[graph[nx][ny]].end is True:
                res.add(''.join(arr+[graph[nx][ny]]))
            dfs(graph, nx, ny, arr+[graph[nx][ny]], res, visit.union({(nx, ny)}), node.children[graph[nx][ny]])


trie = Trie()
W = int(input())
words = [input().strip() for _ in range(W)]

for word in words:
    trie.add(word)

input()
B = int(input())
for b in range(B):
    graph = [[*map(str, input().strip())] for _ in range(4)]
    if b != B-1:
        input()
    
    res = set()
    for i in range(4):
        for j in range(4):
            if graph[i][j] in trie.root.children:
                dfs(graph, i, j, [graph[i][j]], res, {(i, j)}, trie.root.children[graph[i][j]])
    
    hap = 0
    point = [0, 0, 0, 1, 1, 2, 3, 5, 11]
    for word in res:
        hap += point[len(word)]
    max_word = sorted(list(res), key=lambda x: (-len(x), x))[0]
    count = len(res)
    print(hap, max_word, count)
