# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levelMapping = {}
        levelOrder = []


        q = []
        res = []

        if root:
            res.append(root.val)
            q.append(root)
            levelMapping[root] = 0


        while q:
            cur = q.pop(0)
        

            if cur.left:
                q.append(cur.left)
                res.append(cur.left.val)
                levelMapping[cur.left] = levelMapping[cur] + 1
            if cur.right:
                q.append(cur.right)
                res.append(cur.right.val)
                levelMapping[cur.right] = levelMapping[cur] + 1


    
        for node, lvl in levelMapping.items():
            if len(levelOrder) <= lvl:
                levelOrder.append([])
            levelOrder[lvl].append(node.val)
        
        return levelOrder