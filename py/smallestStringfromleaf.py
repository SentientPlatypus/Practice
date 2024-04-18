# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        mp = {}
        q = []
        mp[root] = chr(ord('a') + root.val)
        q.append(root)
        m = "z" * 85

        while q:
            c = q.pop(0)
            if not (c.left or c.right):
                print(mp[c])
                if mp[c] < m:
                    m = mp[c]
            if c.left:
                mp[c.left] = chr(ord('a') + c.left.val) + mp[c]
                q.append(c.left)
            if c.right:
                mp[c.right] = chr(ord('a') + c.right.val) + mp[c]
                q.append(c.right)
        return m

        