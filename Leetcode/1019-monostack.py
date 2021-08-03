# Definition for singly-linked list.
from typing import List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        stack, res = [], []

        while head:
            while stack and head.val > stack[-1][1]:
                res[stack.pop()[0]] = head.val

            stack.append([len(res), head.val])
            res.append(0)
            head = head.next

        return res