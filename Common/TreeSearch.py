class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# BFS.
from collections import deque # Double ended queue.

def BFS(root):
    if root is None:
        return

    queue = deque([root])

    while queue:
        node = queue.popleft()  # dequeue a node from the front of the queue
        print(node.value, end=' ')  # visit the node (print its value in this case)

        # enqueue left child
        if node.left:
            queue.append(node.left)
        # enqueue right child
        if node.right:
            queue.append(node.right)

# DFS.
def DFS(node):
    if node is None:
        return
    # Visit the node (print its value in this case)
    print(node.value, end=' ')
    # Recursively call DFS on the left child
    DFS(node.left)
    # Recursively call DFS on the right child
    DFS(node.right)

# Test.
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print('DFS:')
DFS(root)  # Output: 1 2 4 5 3

print('BFS:')
BFS(root)
