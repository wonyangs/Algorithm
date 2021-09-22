# Solved on 2021. 09. 22.
# 1991 트리 순회

import sys
input = sys.stdin.readline


class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right


def preorderTraversal(node):
    print(node.data, end='')
    if node.left != '.':
        preorderTraversal(tree[node.left])
    if node.right != '.':
        preorderTraversal(tree[node.right])


def inorderTraversal(node):
    if node.left != '.':
        inorderTraversal(tree[node.left])
    print(node.data, end='')
    if node.right != '.':
        inorderTraversal(tree[node.right])


def postorderTraversal(node):
    if node.left != '.':
        postorderTraversal(tree[node.left])
    if node.right != '.':
        postorderTraversal(tree[node.right])
    print(node.data, end='')


N = int(input())
tree = {}

for _ in range(N):
    node, left, right = map(str, input().split())
    tree[node] = Node(data=node, left=left, right=right)

preorderTraversal(tree['A'])
print()
inorderTraversal(tree['A'])
print()
postorderTraversal(tree['A'])
print()

