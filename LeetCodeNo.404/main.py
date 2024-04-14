# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root.left is None and root.right is None:
            return 0
        
        if root.left is not None and root.right is not None:
            return self.goNext(root.left, True) + self.goNext(root.right, False)
        elif root.left is not None:
            return self.goNext(root.left, True)
        else:
            return self.goNext(root.right, False)

    def goNext(self, root, is_left):
        if root is None:
            return 0
        
        if root.left is None and root.right is None:
            if is_left:
                return root.val
            else:
                return 0
        
        return self.goNext(root.left, True) + self.goNext(root.right, False)
        


