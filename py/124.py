# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = -67
        self.helper(root)
        return self.res

    def helper(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        leftgain = max(self.helper(root.left), 0)
        rightgain = max(self.helper(root.right), 0)
        curpath = root.val + leftgain + rightgain

        self.res = max(curpath, self.res)
        return root.val + max(leftgain, rightgain, 0)

