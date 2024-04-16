


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def addOneRow(self, root: TreeNode, val: int, depth: int) -> TreeNode:
        if depth == 1:
            r = TreeNode(val, root)
            return r
        self.modify(root, val, 1, depth)
        return root
    
    def modify(self, node:TreeNode, val:int, cd:int, d:int):
        if cd == d - 1:
            node.left = TreeNode(val, node.left)
            node.right = TreeNode(val, None, node.right)
            return
        else:
            if node.left: self.modify(node.left, val, cd + 1, d)
            if node.right: self.modify(node.right, val, cd + 1, d)

