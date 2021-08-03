class Node:
    def __init__(self, key, val):
        self.value = val
        self.key = key
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.size = capacity
        self.cache = {}
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add(self, node):
        p = self.tail.prev
        p.next = node
        node.prev = p
        self.tail.prev = node
        node.next = self.tail


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self._remove(node)
        self._add(node)
        return node.value


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])

        node = Node(key, value)
        self.cache[key] = node
        self._add(node)
        
        if len(self.cache) > self.size:
            node = self.head.next
            self._remove(node)
            del self.cache[node.key]

    """
    def __init__(self, capacity: int):
        self.dict = collections.OrderedDict()
        self.size = capacity

    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1
        val = self.dict[key]
        # most recently used
        self.dict.move_to_end(key)
        return val

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            del self.dict[key]
        self.dict[key] = value
        if len(self.dict) > self.size:
            self.dict.popitem(last=False)
    """