# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        while root:
            # Both nodes are smaller → LCA is in left subtree
            if p.val < root.val and q.val < root.val:
                root = root.left

            # Both nodes are greater → LCA is in right subtree
            elif p.val > root.val and q.val > root.val:
                root = root.right

             # They split here, or root == p/q
            else:
                return root