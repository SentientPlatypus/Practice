# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []

        curpath = []
        def backtrack(root, cursum):
            if not root:
                return

            cursum += root.val
            
            curpath.append(root.val)
            if cursum == targetSum and (not root.left and not root.right):
                res.append(curpath[:])
            else:
                backtrack(root.left, cursum )
                backtrack(root.right, cursum)
            curpath.pop()
        
        backtrack(root, 0)

        return res
