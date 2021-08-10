# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head or k < 2:
            return head

        next_head = head
        for i in range(1, k):
            next_head = next_head.next
            if not next_head:
                return head

        res = next_head

        cur = head
        while next_head:
            tail = cur
            prev = None
            
            for i in range(k):
                if next_head:
                    next_head = next_head.next
                
                next_node = cur.next # break
                cur.next = prev # reverse
                prev = cur # increment
                cur = next_node # increment

            tail.next = next_head or cur

        return res