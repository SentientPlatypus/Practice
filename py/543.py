# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        if not root:
            return 0
        
        self.maxdepth(root)
        return self.res


    def maxdepth(self, root):
        if not root:
            return 0

        leftdepth = self.maxdepth(root.left)
        rightdepth = self.maxdepth(root.right)

        curdiam = leftdepth + rightdepth
        self.res = max(self.res, curdiam)

        return 1 + max(leftdepth, rightdepth)
        
        
