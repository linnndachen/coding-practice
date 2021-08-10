class Solution:
    """
    def lengthOfLIS(self, nums):
        dp = []
        for elem in nums:
            idx = bisect_left(dp, elem)
            if idx == len(dp):
                dp.append(elem)
            else:
                dp[idx] = elem
        return len(dp)
    """
    def lengthOfLIS(self, nums):
        """
        (1) if x is larger than all tails, append it, increase the size by 1
        (2) if tails[i-1] < x <= tails[i], update tails[i]
        """
        def _binsearch(lst, target):
            lo, hi = 0, len(lst)
            while lo < hi:
                mid = (lo+hi) // 2
                
                if lst[mid] < target:
                    lo = mid+1
                else:
                    hi = mid
            return lo

        tails = []

        for num in nums:
            if not tails or num > tails[-1]:
                tails.append(num)
            else:
                idx = _binsearch(tails, num)
                tails[idx] = num
        return len(tails)


    """
    def lengthOfLIS(self, nums: List[int]) -> int:
        # note: I tried stack but cannot use it. See example 2
        if not nums:
            return 0
        
        n = len(nums)
        
        #dp[i] = the longest seq if we only have i numbers
        dp = [1 for _ in range(n)]
        
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], 1+dp[j])

        return max(dp)
    """