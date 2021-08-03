import random
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.root = head
        self.n = 1

        node = self.root
        while node.next:
            node = node.next
            self.n += 1


    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        idx = random.random() * self.n
        i = 1
        node = self.root
        while i <= idx:
            node = node.next
            i += 1

        return node.val