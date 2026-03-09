class ListNode:
    def __init__(self, key:int, value:int, prev:ListNode, nxt:ListNode):
        self.k = key
        self.v = value
        self.p = prev
        self.n = nxt


class LRUCache:

    def print_list(self, head):
        current = head
        while current:
            print(current.k, end=" <-> ")
            current = current.n

    def __init__(self, capacity: int):
        self.d = {}
        self.s = 0
        self.cap = capacity
        
        self.hd = None
        self.tl = None

    def move_to_front(self, node:ListNode):
        if self.hd.k == node.k and self.tl.k == node.k:
            #only node in the list, do nothing, already at front
            return
        elif self.hd.k == node.k:
            #already at front
            return
        elif self.tl.k == node.k:

            if node.p:
                self.tl = node.p
                node.p.n = None
        else:
            if node.p:
                node.p.n = node.n
            if node.n:
                node.n.p = node.p

        self.hd.p = node
        node.n = self.hd
        node.p = None
        self.hd = node


    def get(self, key: int) -> int:
        if key in self.d.keys():
            node = self.d[key]
            self.move_to_front(node)
            return node.v
        return -1

    def put(self, key: int, value: int) -> None:
        node:ListNode

        if key in self.d.keys():
            node = self.d[key]
            node.v = value
        else:
            # must create a new node, and insert before the head
            node = ListNode(key, value, None, None)
            
            if not self.hd:
                self.hd = node
                self.tl = node

            if self.s < self.cap:
                self.s += 1
            elif self.s == self.cap:
                keyToRemove = self.tl.k 
                self.d.pop(keyToRemove) #remove the key at the tail from dict.

                if self.tl.p:
                    self.tl = self.tl.p
                    self.tl.n = None
                else:
                    #tail and head are the same
                    self.tl = node


            self.d[key] = node

        self.move_to_front(node)


        

            
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
