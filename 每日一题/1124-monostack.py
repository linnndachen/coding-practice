from typing import List
class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        # stack solution
        n = len(hours)
        prev, count = [0], 0
        # count means total(tiring) - total(non-tiring) up until i days

        #          [9, 9, 6, 0,  6,  6,  9]
        # prev: [0, 1, 2, 1, 0, -1, -2, -1]
        for idx, n in enumerate(hours):
            count = count + 1 if n > 8 else count - 1
            prev.append(count)

        # the following logic is the same as 962
        stack = []
        # stack means all possible i
        # stack = [0, -1, -2]
        for idx, num in enumerate(prev):
            if not stack or prev[stack[-1]] > num:
                stack.append(idx)

        # find prev[i-1] < prev[j]
        res = 0
        for j in range(len(prev))[::-1]:
            while stack and prev[stack[-1]] < prev[j]:
                res = max(res, j-stack[-1])
                stack.pop()

        return res

    """
    def longestWPI(self, hours: List[int]) -> int:
        # presum solution
        score, res = 0, 0
        seen = {}
        for i, h in enumerate(hours):
            score = score + 1 if h > 8 else score - 1
            if score > 0:
                res = max(res, i + 1)
            else:
                if score - 1 in seen:
                    res = max(res, i - seen[score-1])

                if score not in seen:
                    # 在 i day, how many tiring day is more than non-tiring day
                    seen[score] = i

        return res
    """