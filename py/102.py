# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        q = deque()
        q.append((root, 0))

        while q:
            cur, dpth = q.popleft()
            if cur:
                if dpth < len(res):
                    res[dpth].append(cur.val)
                else:
                    res.append([cur.val])
                
                q.append((cur.left, dpth + 1))
                q.append((cur.right, dpth + 1))

        return res


        
