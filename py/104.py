# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)

        return 1 + max(leftDepth, rightDepth)




#### OR

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        stk = [(root, 1)]
        maxdepth = 0

        while stk:
            cur, depth = stk.pop()

            if cur:
                maxdepth = max(depth, maxdepth)

                stk.append((cur.left, depth + 1))
                stk.append((cur.right, depth + 1))

        return maxdepth
