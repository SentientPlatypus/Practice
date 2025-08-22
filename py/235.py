# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def contains(self, root: TreeNode, target: TreeNode):
        if root.val == target.val:
            return True
        
        inLeft = False
        inRight = False
        if root.left:
            inLeft = self.contains(root.left, target)
        if root.right:
            inRight = self.contains(root.right, target)
        
        return inLeft or inRight


    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        inRoot = self.contains(root, p) and self.contains(root, q)
        inLeft = root.left and self.contains(root.left, p) and self.contains(root.left, q)
        inRight = root.right and self.contains(root.right, p) and self.contains(root.right, q)
        if inRoot:
            if inLeft:
                return self.lowestCommonAncestor(root.left, p, q)
            elif inRight:
                return self.lowestCommonAncestor(root.right, p, q)
            else:
                return root
        return None



