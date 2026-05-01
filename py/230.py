class Solution:
    def inOrder(self, root:Optional[TreeNode]):
        if not root:
            return
        
        self.inOrder(root.left)

        self.trav.append(root.val)

        self.inOrder(root.right)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.trav = []

        self.inOrder(root)
        print(self.trav)
        return self.trav[k - 1]



class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stk = []
        stk.append(root)
        cur = root
        while stk or cur:
            while cur:
                stk.append(cur)
                cur = cur.left
        
            cur = stk.pop()
            k -= 1
            if k == 0:
                return cur.val
            cur = cur.right
