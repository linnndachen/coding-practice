from typing import List

class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        # keep a decreasing stack - monostack
        # left subtree will always append to the stack
        # when visiting the right subtree
        # chk will point to the parent node of the right subtree
        chk, stack = None, []
        for n in preorder:
            while stack and n > stack[-1]:
                chk = stack.pop()
            if chk != None and n < chk:
                return False
            stack.append(n)
        return True
    """
    def verifyPreorder(self, preorder):
        # stack = preorder[:i], reuse preorder as stack
        lower = -1 << 31
        i = 0
        for x in preorder:
            if x < lower:
                return False
            # right tree
            while i > 0 and x > preorder[i - 1]:
                # lower is the left child, then parent
                lower = preorder[i - 1]
                print(i, lower)
                # i is the left idx, then parent
                i -= 1
            # the parent node position will be set to 
            # the largest node on this left subtree/left subtree's right node
            preorder[i] = x
            i += 1
        return True

        """