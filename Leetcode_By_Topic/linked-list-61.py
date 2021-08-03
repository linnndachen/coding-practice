# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next:
            return head

        last, n = head, 1
        while last.next:
            last = last.next
            n += 1

        # edge case
        if k % n == 0:
            return head

        mid = head
        for i in range(n- k%n - 1):
            mid = mid.next

        # only need to reconnect 3 nodes
        new_head = mid.next
        last.next = head
        mid.next = None
        
        return new_head