from typing import List
class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        # [6,0,8,2,1,5]
        # stack = [6, 0]
        stack, res = [], 0
        for i, num in enumerate(A):
            if not stack or A[stack[-1]] > num:
                stack.append(i)

        # iterate from the back
        # if 0 and 5 is valid, we don't need to check 0 and 1 or anything before
        # because 0 and 5 must be the longest pair
        for j in range(len(A))[::-1]:
            while stack and A[stack[-1]] <= A[j]:
                res = max(res, j - stack.pop())

        return res

    """
    def maxWidthRamp(self, A: List[int]) -> int:
        # nlogn
        stack,res = [], 0

        for i in range(len(A))[::-1]:
            if not stack or A[i] > stack[-1][0]:
                stack.append([A[i], i])
            else:
                pos = bisect.bisect(stack, [A[i], i])
                j = stack[pos][1]
                res = max(res, abs(j-i))

        return res

    def maxWidthRamp(self, A: List[int]) -> int:
        # [9,8,1,0,1,9,4,0,4,1]
        # [5,4,7,4,/,/,2,/,/]
        # O N^2
        memo = {}
        for idx, num in enumerate(A):
            if num in memo:
                continue

            for j in range(idx, len(A)):
                if A[j] >= A[idx]:
                    memo[num] = j - idx

        return max(memo.values())
    """