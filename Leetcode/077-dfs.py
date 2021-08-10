from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        self.backtrack(n, k,[], 1, res)
        return res

    def backtrack(self, n, k, path, idx, res):
        if len(path) == k:
            res.append(path[:])
            return 
        
        for num in range(idx, n+1):
            path.append(num)
            self.backtrack(n, k, path, num+1, res)
            path.pop()

class Solution2:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # init first combination
        # the[n+1] is a sentinel
        nums = list(range(1, k + 1)) + [n + 1]

        output, j = [], 0
        while j < k:
            output.append(nums[:k])
            # increase first nums[j] by one
            # if nums[j] + 1 != nums[j + 1]
            j = 0
            # if left and right pointer right next to each other
            while j < k and nums[j + 1] == nums[j] + 1:
                # move the right pointer
                nums[j] = j + 1
                j += 1
            # else, move the left pointer
            nums[j] += 1
            
        return output