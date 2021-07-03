class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        res, total = 0, 0
        satisfaction.sort()
        # [-9,-8,-1,0,5], res = 5+5+4
        # [2,3,4] res = 4+7+9
        while satisfaction and satisfaction[-1] + total > 0:
            total += satisfaction.pop()
            res += total
        return res