class Solution(object):
    def checkEqualTree(self, root):
        # Stores the sum of all leaves for each node in the tree.
        seen = []

        # DFS 
        def sum_(node):
            if not node:
                return 0
            seen.append(sum_(node.left) + sum_(node.right) + node.val)
            return seen[-1] # The sum of all leaves for the root of the tree.

        total = sum_(root)
        seen.pop()
        return total / 2.0 in seen
