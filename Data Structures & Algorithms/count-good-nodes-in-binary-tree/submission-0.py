# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, maxValue):
            if node is None:
                return 0

            count = 0

            #current node is good
            if node.val >= maxValue:
                count = 1

            maxValue = max(maxValue, node.val)

            count += dfs(node.left, maxValue)
            count += dfs(node.right, maxValue)

            return count

        return dfs(root, root.val)