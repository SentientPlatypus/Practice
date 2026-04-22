# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True
        self.depth(root)
        return self.balanced
    

    def depth(self, root):
        if not root:
            return 0
        
        ldepth = self.depth(root.left)
        rdepth = self.depth(root.right)

        if abs(ldepth - rdepth) > 1:
            self.balanced = False
        
        return 1 + max(ldepth, rdepth)
