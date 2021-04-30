class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        # store the index of small numbers
        stack = []

        for i, val in enumerate(A):
            if not stack or val < A[stack[-1]]:
                stack.append(i)      
        maxWidth = 0
        # from the furthest possible distance
        for i in range(len(A)-1, -1, -1):
            val = A[i]
            # if val > than the smallest num in the stack
            while stack and val >= A[stack[-1]]:
                maxWidth = max(maxWidth, i - stack.pop())

        return maxWidth