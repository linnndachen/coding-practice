from collections import defaultdict
import random

class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.table = defaultdict(set)
        self.lst = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """

        self.table[val].add(len(self.lst))
        self.lst.append(val)

        return len(self.table[val]) == 1

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if not self.table[val]:
            return False

        index = self.table[val].pop()
        last = self.lst[-1]

        self.lst[index] = last

        self.table[last].add(index)
        self.table[last].remove(len(self.lst)-1)

        self.lst.pop()
        return True

        remove_idx, last_elem = self.dict[val].pop(), self.lst[-1]
        self.lst[remove_idx] = last_elem
        self.dict[last_elem].add(remove_idx)
        self.dict[last_elem].discard(len(self.lst) - 1)

        self.lst.pop()
        return True


    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return random.choice(self.lst)



# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()