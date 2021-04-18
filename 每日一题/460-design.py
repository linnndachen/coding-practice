class Node:
    def __init__(self, key, val):
        self.value = val
        self.key = key
        self.freq = 1
        self.next = None
        self.prev = None

class DDL:
    def __init__(self):
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.size = 0

        self.head.next = self.tail
        self.tail.prev = self.head


    def pop(self, node=None):
        if self.size == 0:
            return

        if not node:
            node = self.tail.prev

        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1

        return node

    def insertHead(self, node):
        cur_head = self.head.next
        node.next = cur_head
        cur_head.prev = node

        self.head.next = node
        node.prev = self.head
        self.size += 1

class LFUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.minFreq = 1

        self.cache = {}
        self.freq_table = collections.defaultdict(DDL)

    def _updateFreq(self, node):
        old_freq = node.freq
        self.freq_table[old_freq].pop(node)

        if self.minFreq == old_freq and self.freq_table[old_freq].size == 0:
            self.minFreq += 1

        node.freq += 1
        cur_freq = node.freq
        self.freq_table[cur_freq].insertHead(node)


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self._updateFreq(node)
        return node.value
    
    def put(self, key: int, value: int) -> None:
        if self.size <= 0:
            return 

        if key in self.cache:
            node = self.cache[key]
            self.get(key)
            node.value = value
        else:
            if len(self.cache) >= self.size:
                node = self.freq_table[self.minFreq].pop()
                del self.cache[node.key]

            new_node = Node(key, value)
            self.cache[key] = new_node
            self.freq_table[1].insertHead(new_node)
            self.minFreq = 1



"""
class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        # {key: (val, freq)}
        self.cache = {}
        # E.g. { freq 1 : {2 : None, 4 : None, 6: None}, freq 2 : {1 : None, 3 : None, 5 : None} }
        self.freq_table = collections.defaultdict(OrderedDict)
        self.minFreq = 1

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        val, freq = self.cache.pop(key)
        self.cache[key] = (val, freq + 1)

        self.freq_table[freq].pop(key)
        if len(self.freq_table[freq]) == 0 and freq == self.minFreq:
            self.minFreq += 1

        self.freq_table[freq+1][key] = None
        return val

    def put(self, key: int, value: int) -> None:
        if self.capacity <= 0:
            return

        if key in self.cache:
            self.get(key) # Update the key freq in dict
            self.cache[key] = (value, self.cache[key][1])
            return

        if self.capacity <= len(self.cache):
            delKey, _ = self.freq_table[self.minFreq].popitem(last=False) # pop first
            self.cache.pop(delKey)

        self.cache[key] = (value, 1)
        self.freq_table[1][key] = None 
        self.minFreq = 1

"""
# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)