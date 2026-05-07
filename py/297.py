# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "_"
        
        res = []
        stk = [root]
        
        while stk:
            cur = stk.pop()
            if cur:
                res.append(str(cur.val))
                stk.append(cur.right)
                stk.append(cur.left)
            else:
                res.append("_") 
            
        return ",".join(res)

        

    def deserialize(self, data):
        vals = data.split(",")
        self.i = 0
        
        def dfs():
            if vals[self.i] == "_":
                self.i += 1
                return None
            
            node = TreeNode(int(vals[self.i]))
            self.i += 1

            node.left = dfs()
            node.right = dfs()
            return node
            
        return dfs()
        

        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
