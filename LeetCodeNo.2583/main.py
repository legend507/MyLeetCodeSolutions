# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        # Thoughts:
        # Use DFS to create a dict, with key = level, val = a list of all values on this level.
        # Traverse the dict, calc sums of each level.
        # Find kth.
        
        level = {}

        def DFS(node, level_indicator):
            if node is None:
                return

            if level_indicator in level:
                level[level_indicator].append(node.val)
            else:
                level[level_indicator] = [node.val]

            DFS(node.left, level_indicator + 1)
            DFS(node.right, level_indicator + 1)

        DFS(root, 0)
        
        level_sum = []
        for _, val in level.items():
            level_sum.append(sum(val))
        
        level_sum.sort(reverse=True)

        return level_sum[k-1] if k-1 <len(level_sum) else -1
    