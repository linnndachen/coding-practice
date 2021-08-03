class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:        
        def _check(candy):
            # we havn't hit one yet  |||
            if candy > index:
                # （首位+末项）* 项数 / 2
                l = (candy - index + candy) * (index + 1)// 2
            else: # we have extra ones ...|||
                # （首相+末项）* 项数 / 2  + 多出来的1
                l = (1+candy) * candy // 2 + (index + 1 - candy)

            if candy > n - index:
                r = (candy - (n-index) + 1 + candy) * (n - index) // 2
            else:
                # （首相+末项）* 项数 / 2  + 多出来的1
                r = (1+candy) * candy // 2 + (n - (index+candy) )

            return r + l - candy

        left, right = 1, maxSum
        while left < right:
            mid = (left + right) // 2 + 1
            if _check(mid) <= maxSum:
                left = mid
            else:
                right = mid - 1
        return left