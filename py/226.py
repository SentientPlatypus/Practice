# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root or not (root.left or root.right):
            return root

        root.right = self.invertTree(root.right)
        root.left = self.invertTree(root.left)

        tmp = root.left
        root.left = root.right
        root.right = tmp

        return root
