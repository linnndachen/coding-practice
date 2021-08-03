class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        n = len(nums)
        pre_sum = [0] * (n + 1)
        
        for i in range(n):
            pre_sum[i+1] = pre_sum[i] + nums[i]

        stack, res = [], 0
        for i in range(n+1):
            while stack and (i == n or nums[stack[-1]] > nums[i]):
                min_val = nums[stack.pop()]
                arr_sum = pre_sum[i]-pre_sum[stack[-1]+1] if stack else pre_sum[i]
                
                res = max(res, min_val * arr_sum)
            
            stack.append(i)
        
        return res % 1000000007