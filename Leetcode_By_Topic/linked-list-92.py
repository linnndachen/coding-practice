# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if not head or left == right: 
            return head

        # p is the last_node_before_reversal
        p = dummy = ListNode(None)
        dummy.next = head

        # go to the correct position
        for i in range(left-1): 
            p = p.next

        # first node of the reversal list should come out as the tail
        tail = p.next

        for i in range(right - left):
            tmp = p.next                  # a) cache a node
            p.next = tail.next            # b) cut out the cache node
            tail.next = tail.next.next    # c) connect the cut-out node to next pointer
            p.next.next = tmp             # d) connect the cut-out node to previous pointers

        return dummy.next