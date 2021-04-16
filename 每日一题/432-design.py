class Node(object):
    def __init__(self, val, prev=None, next=None):
        # val is frequency
        self.val = val
        self.prev = prev
        self.next = next
        # all the keys in "val"/ x freq
        self.keys = set()

class AllOne:

    def __init__(self):
        self.head = Node(0)
        self.tail = Node(0, self.head)
        self.head.next = self.tail
        self.mapping = defaultdict(lambda: self.head)

    def inc(self, key: str) -> None:
        cur = self.mapping[key]
        # remove from current bucket
        cur.keys.discard(key)
        
        # new freq exist
        if cur.val + 1 == cur.next.val:
            new = cur.next
        else: # insert a new bucket
            new = Node(cur.val + 1, cur, cur.next)
            new.prev.next = new.next.prev = new
        
        new.keys.add(key)
        self.mapping[key] = new
        
        # if after remove, the bucket is empty
        if not cur.keys and cur.val != 0:
            cur.prev.next, cur.next.prev = cur.next, cur.prev
            
    def dec(self, key: str) -> None:
        if not key in self.mapping: 
            return
        
        cur = self.mapping[key]
        cur.keys.discard(key)
        self.mapping.pop(key)
        
        if cur.val > 1:
            # if belongs to the lower bucket
            if cur.val - 1 == cur.prev.val:
                new = cur.prev
            else: # insert a new bucket before the lower bucket
                new = Node(cur.val - 1, cur, cur.next)
                new.prev.next = new.next.prev = new
                
            new.keys.add(key)
            self.mapping[key] = new

        if not cur.keys:
            cur.prev.next, cur.next.prev = cur.next, cur.prev

    def getMaxKey(self) -> str:
        if not self.tail.prev.val: 
            return ''
        
        # pop and add back to get arbitrary (but not random) element
        key = self.tail.prev.keys.pop()
        self.tail.prev.keys.add(key)
        return key

    def getMinKey(self) -> str:
        if not self.head.next.val: 
            return ''
        
        key = self.head.next.keys.pop()
        self.head.next.keys.add(key)
        return key


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()