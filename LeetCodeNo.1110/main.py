# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        
        # Use BFS to find nodes to delete.
        # deque stores [node, node's parent].
        # if current node is in to_delete, process child and parent.
        # other wise, this node maybe a root.

        ret = []

        from collections import deque

        parent = None
        queue = deque()
        queue.append([root, None])

        while queue:
            element = queue.popleft()
            node, parent = element[0], element[1]
            
            # Delete current node.
            if node.val in to_delete:
                # Append this node's childen in BFS queue, but parent = None.
                if node.left:
                    queue.append([node.left, None])
                if node.right:
                    queue.append([node.right, None])

                # Change parent's either left or right to None.                
                if parent:
                    if parent.left == node:
                        parent.left = None
                    else:
                        parent.right = None
            else:
                # Not in t_delete, and no parent, meaning a root.
                if parent == None:
                    ret.append(node)

                # Add this node's right and left to BFS queue.
                if node.left:
                    queue.append([node.left, node])
                if node.right:
                    queue.append([node.right, node])
        return ret
    
