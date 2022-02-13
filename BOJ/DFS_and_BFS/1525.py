# Solved on 2022. 2. 13.
# 1525 퍼즐

from collections import deque
import sys
input = sys.stdin.readline


def incoding(graph):
    string = ""
    for g in graph:
        g = [*map(str, g)]
        string += "".join(g)
    return string

def swap(string, n):    
    return string.translate(str.maketrans('0'+n, n+'0'))

def bfs(string):
    queue = deque()
    queue.append((string, 0))
    visit = set()
    visit.add(string)
    d = [[1,3], [0,2,4], [1,5], 
         [0,4,6], [1,3,5,7], [2,4,8], 
         [3,7], [4,6,8], [5,7]]
    
    while queue:
        string, count = queue.popleft()
        if string == end:
            print(count)
            return
        for nxt in d[string.find('0')]:
            new_string = swap(string, string[nxt])
            if new_string not in visit:
                queue.append((new_string, count+1))
                visit.add(new_string)
    print(-1)


graph = [[*map(int, input().split())] for _ in range(3)]
string = incoding(graph)
end = '123456789'
for i in range(1, 10):
    if str(i) not in string:
        end = swap(end, str(i))
        break
bfs(string)
