class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        """
        For each A[i], find out the maximum A[j]
        that A[i] + A[j] <= target.

        For each elements in the subarray A[i+1] ~ A[j],
        we can pick or not pick,
        so there are 2 ^ (j - i) subsequences in total.
        So we can update res = (res + 2 ^ (j - i)) % mod
        """
        # while subsequence order does matter
        # here we only care about the min and max
        nums.sort()
        l, r = 0, len(nums) - 1
        res = 0
        # in case of overflow
        mod = 10**9 + 7
        while l <= r:
            if nums[l] + nums[r] > target:
                r -= 1
            else:
                # same as : res += 2 ** (r - l), res %= mod
                # write it this way otherwise will overflow
                res += pow(2, r - l, mod)
                l += 1
        return res % mod