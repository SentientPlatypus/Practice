# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEqual(self, a:Optional[TreeNode], b:Optional[TreeNode]):
        if not a and not b:
            return True
        if (a and not b) or (b and not a) or (a.val != b.val):
            return False
        return self.isEqual(a.left, b.left) and self.isEqual(a.right, b.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if self.isEqual(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
