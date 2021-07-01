# Definition for singly-linked list.
import heapq
from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None

        heap = []

        head = cur = ListNode(-1)
        for i, node in enumerate(lists) :
            if node:
                heapq.heappush(heap, (node.val, i, node))

        while heap:
            _, i, node = heapq.heappop(heap)
            cur.next = node
            cur = cur.next
            node = node.next

            if node:
                heapq.heappush(heap, (node.val, i, node))

        return head.next