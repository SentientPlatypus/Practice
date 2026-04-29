# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.prev = -float('inf')
        return self.inOrder(root)
    
    def inOrder(self, root:Optional[TreeNode]):
        if not root:
            return True

        l = self.inOrder(root.left)
        
        if not l:
            return False
        
        if root.val <= self.prev:
            return False
        self.prev = root.val

        return self.inOrder(root.right)
