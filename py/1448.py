class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0

        stk = []
        stk.append((root, root.val))

        while stk:
            cur, curmax = stk.pop()

            if cur:
                if cur.val >= curmax:
                    res += 1
                    curmax = cur.val
                
                stk.append((cur.left, curmax))
                stk.append((cur.right, curmax))
        return res
                
