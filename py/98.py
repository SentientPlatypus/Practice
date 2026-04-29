# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.traversal = []
        self.inOrder(root)
        for i in range(1, len(self.traversal)):
            if self.traversal[i] <= self.traversal[i - 1]:
                return False
        return True
    
    def inOrder(self, root:Optional[TreeNode]):
        if not root:
            return None

        self.inOrder(root.left)
        self.traversal.append(root.val)
        self.inOrder(root.right)

        
