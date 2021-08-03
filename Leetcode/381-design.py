from collections import defaultdict
from random import choice

class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.lst = []
        self.dict = defaultdict(set)


    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """

        # instead of = one value, add the new position to the set
        self.dict[val].add(len(self.lst))
        self.lst.append(val)
        return len(self.dict[val]) == 1


    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if not self.dict[val]: 
            return False
        
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
        return choice(self.lst)