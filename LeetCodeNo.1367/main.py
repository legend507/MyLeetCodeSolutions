# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.storage = []
        # self.found = False

    def _DFS(self, root, current_path): # Note that current_path is passed by reference, not by value. I want to pass by value here.

        # Break out condition.
        if root == None:
            return
        
        current_path.append(str(root.val))
        self.storage.append(current_path)

        self._DFS(root.left, current_path.copy())
        self._DFS(root.right, current_path.copy())


    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        current_path = []

        self._DFS(root, current_path)

        pointer = head
        to_find = ''
        while pointer != None:
            to_find += str(pointer.val)
            pointer = pointer.next

        for one_path in self.storage:
            target = ''.join(one_path)

            if target.find(to_find) != -1:
                return True
        return False