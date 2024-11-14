# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        q = [root]
        if root:
            mp = {root : root.val}

        while q:
            c = q.pop()
            if c:
                if (not c.left and not c.right and mp[c] == targetSum): return True

                if c.left:
                    q.append(c.left)
                    mp[c.left] = mp[c] + c.left.val
                if c.right:
                    q.append(c.right)
                    mp[c.right] = mp[c] + c.right.val
        return False

