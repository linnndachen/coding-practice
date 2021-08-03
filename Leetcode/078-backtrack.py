class Solution:  
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        n = len(nums)
        for k in range(n + 1):
            self.backtrack(0, [], k, output, nums)
        return output

    def backtrack(self, start, curr, k, output, nums):
        if len(curr) == k:  
            output.append(curr[:])
            return
        for i in range(start, len(nums)):
            curr.append(nums[i])
            self.backtrack(i + 1, curr, k, output, nums)
            curr.pop()


        """
        # saves space as well
        def explore(cur, remaining, res):
            if not remaining:
                res.append(cur[:])
                return
            
            d = remaining.pop(0)
            #choose
            cur.append(d)
            
            #explore
            explore(cur, remaining, res)
            cur.pop()
            explore(cur, remaining, res)
            #unchoose
            remaining.insert(0, d)

        res = []
        explore([], nums, res)
        return res
        """
        """
        # Cascading
        # O(n * 2^N) - Time
        # O(n * 2^N) - Space
        nums.sort()
        subsets = [[]]

        for num in nums:
            subsets += [i + [num] for i in subsets]

        return subsets
        """