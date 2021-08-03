class RandomizedSet:
    def __init__(self) -> bool:
        """
        Initialize your data structure here.
        """
        self.dict = {}
        self.data = []


    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.dict:
            return False
 
        self.dict[val] = len(self.data)
        self.data.append(val)

        return True



    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.dict:
            return False

        last_elem = self.data[-1]
        index_to_remove = self.dict[val]
        
        self.dict[last_elem] = index_to_remove
        self.data[index_to_remove] = last_elem

        self.data[-1] = val
        self.data.pop()
        self.dict.pop(val)

        return True


    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.data)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()