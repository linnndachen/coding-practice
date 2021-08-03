from typing import List
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if len(nums) < k:
            return False

        nums.sort(reverse=True)
        total = sum(nums)
        if total % k != 0:
            return False

        target = total // k
        visited = [0] * 16
    
        def _dfs(idx, group,cur_sum):
            if group == k:
                return True

            if cur_sum > target:
                return False

            if cur_sum == target:
                return _dfs(0, group+1, 0)

            prev_n = -1
            for i in range(idx, len(nums)):
                if visited[i] == 1:
                    continue

                # skip duplicate
                if nums[i] == prev_n:
                    continue

                visited[i] = 1
                prev_n = nums[i]

                if _dfs(i+1, group, cur_sum + nums[i]):
                    return True

                visited[i] = 0

            return False

        return _dfs(0, 0, 0)