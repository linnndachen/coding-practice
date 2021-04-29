class Solution:
    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n, total = len(nums), sum(nums)
        if total % 4 != 0 or n < 4:
            return False

        self.memo = {}
        return self.dfs(nums, (1<<n)-1, total//4, 0)
        
    def dfs(self, nums, mask, side_len, sides_done):
        n = len(nums)

        # the total sums of matchsticks used till now
        used = 0
        for i in range(n-1, -1, -1):
            if not (mask & (1 << i)):
                used += nums[n-1-i]

        if used > 0 and used % side_len == 0:
            sides_done += 1

        if sides_done == 3:
            return True

        if (mask, sides_done) in self.memo:
            return self.memo[(mask, sides_done)]

        res = False

        # matchsticks for each completed sides
        count = used // side_len
        # how many empty spaces we have for the incompleted side
        left = side_len * (count+1) - used

        for i in range(n-1, -1, -1):
            # if the current one fits the remaining space
            # and it has not been used
            if nums[n-1-i] <= left and mask&(1 << i):
                # mask ^ (1 << i) makes the i^th from the right, 
                # 0 making it unavailable in future recursions. 
                if self.dfs(nums, mask ^ (1<<i), side_len, sides_done):
                    res = True
                    break

        self.memo[(mask, sides_done)] = res
        return res



    """
    # backtracking 4^N
    def makesquare(self, nums: List[int]) -> bool:
        n, total = len(nums), sum(nums)

        if total % 4 != 0 or n < 4:
            return False
        nums.sort(reverse=True)
        self.sums = [0 for _ in range(4)]

        return self.backtracking(nums, total // 4, 0)

    def backtracking(self, nums, target, idx):
        n = len(nums)
        if idx == n:
            return self.sums[0] == self.sums[1] == self.sums[2] == target

        for i in range(4):
            if self.sums[i] + nums[idx] <= target:
                self.sums[i] += nums[idx]
                
                if self.backtracking(nums, target, idx+1):
                    return True
                self.sums[i] -= nums[idx]
        return False
    """