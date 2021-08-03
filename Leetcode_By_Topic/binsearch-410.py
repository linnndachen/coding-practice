class Solution:
    """
    # TLE using dp, better use binary search
    # Time - O(n^2 * m)
    def splitArray(self, nums: List[int], m: int) -> int:
        n = len(nums)
        memo = {}

        def dfs(idx, m):
            if idx == n:
                return 0
            if m == 1:
                res = sum(nums[idx:])
                return res

            if (idx, m) in memo:
                return memo[(idx, m)]

            res = float('inf')
            # pay attention to the twist here
            for j in range(1, n-1):
                left = sum(nums[idx:idx+j])
                right = dfs(idx+j, m-1)
                res = min(res, max(left, right))

            memo[(idx, m)] = res
            return res

        return dfs(0, m)

    """
    # binary search
    # Time (n * log(sum of array))
    def splitArray(self, nums: List[int], m: int) -> int:
        maxi, total = 0 , 0
        for num in nums:
            total += num
            if num > maxi:
                maxi = num

        left, right = maxi, total
        while left < right:
            mid = (left + right) // 2
            counts = self._countA(mid, nums, m)
            if counts <= m:
                right = mid
            else:
                left = mid + 1
        return left

    def _countA(self, altSum, nums, m):
        # if count <= m, res potentially < altSum
        # if count > m, res > altSum
        count = 1
        cur_sum = 0
        for num in nums:
            if (num + cur_sum) <= altSum:
                cur_sum += num

            else:
                count += 1
                cur_sum = num
        
        return count