class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:        
        need = sum(nums) % p
        dic, n = {0:-1}, len(nums)
        cur, res = 0, n
        for i, num in enumerate(nums):
            cur = (cur + num) % p
            dic[cur] = i
            if (cur - need) % p in dic:
                res = min(res, i - dic[(cur-need) % p])
        return res if res < n else -1